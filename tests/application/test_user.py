from pytest import raises

from src.business.application.user import dto, exceptions, use_cases


class TestUser:
    id = 1
    name = "John"
    surname = "Doe"
    email = "email@email.com"

    async def test_create_user(
        self,
        create_user: use_cases.CreateUser,
    ) -> None:
        user_id = await create_user(
            dto.UserCreate(
                self.name,
                self.surname,
                self.email,
            )
        )

        assert user_id == self.id

    async def test_get_user(self, get_user: use_cases.GetUser) -> None:
        user = await get_user(self.id)

        assert user.name == self.name
        assert user.surname == self.surname
        assert user.email == self.email

        with raises(exceptions.UserNotExists):
            await get_user(10000)

    async def test_update_user(
        self,
        update_user: use_cases.UpdateUser,
    ) -> None:
        new_name = "Bill"
        new_surname = "Marker"
        new_email = "newmail@mail.com"

        user = await update_user(dto.UserUpdate(self.id))

        assert user.id == self.id
        assert user.name == self.name
        assert user.surname == self.surname
        assert user.email == self.email

        user = await update_user(dto.UserUpdate(self.id, new_name))

        assert user.name == new_name
        assert user.surname == self.surname
        assert user.email == self.email

        user = await update_user(
            dto.UserUpdate(
                self.id,
                new_name,
                new_surname,
            )
        )

        assert user.name == new_name
        assert user.surname == new_surname
        assert user.email == self.email

        user = await update_user(
            dto.UserUpdate(
                self.id,
                new_name,
                new_surname,
                new_email,
            )
        )

        assert user.name == new_name
        assert user.surname == new_surname
        assert user.email == new_email

        with raises(exceptions.UserNotExists):
            await update_user(dto.UserUpdate(10000))
