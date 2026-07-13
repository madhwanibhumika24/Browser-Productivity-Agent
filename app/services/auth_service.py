from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserRegister, UserLogin
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token


class AuthService:
    """
    Service responsible for user authentication.
    """

    @staticmethod
    def register_user(db: Session, user: UserRegister) -> User:

        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            raise ValueError("Email already registered.")

        hashed_password = hash_password(user.password)

        new_user = User(
            full_name=user.full_name,
            email=user.email,
            password=hashed_password
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def login_user(db: Session, user: UserLogin):

        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if not existing_user:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            user.password,
            existing_user.password
        ):
            raise ValueError("Invalid email or password.")

        access_token = create_access_token(
            {
                "sub": existing_user.email,
                "user_id": existing_user.id
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }