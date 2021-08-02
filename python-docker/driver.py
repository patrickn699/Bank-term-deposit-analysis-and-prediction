pip install fastapi, uvicorn[standard]


from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello!..Please enter you name"


@app.get("/names/{item_id}")
def read_item(item_id: str):
    return "Hey"+ ' ' +str(item_id)+"!"+' '+"welcome to FastAPI"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)