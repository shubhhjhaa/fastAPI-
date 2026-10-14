from fastapi import FastAPI, status

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = 404,
            deatil ="user not found"
        )