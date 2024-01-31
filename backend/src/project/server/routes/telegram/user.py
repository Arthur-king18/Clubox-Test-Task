from fastapi.responses import HTMLResponse

from backend.src.project.db.models import User
from backend.src.project.server import app


async def generate_html_response(name: str, age: int, count_user: int) -> HTMLResponse:
    html_content = f"""
    <html>
        <head>
          <style>
            body {{
              background-color: white;
              color: black;
              font-size: 30px;
              text-align: center;
            }}
          </style>
          
            <title>Welcome {name}</title>
        </head>
        <body>
            <h1><b>Successful registration !</b></h1>
            <h2>Your name is {name}</h2>
            <h2>Your age is {age}</h2>
            <h2>Numbers of users {count_user}</h2>
        </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)


@app.get('/api/telegram/user/{user_id}', response_class=HTMLResponse)
async def get_user_info(user_id: str):
    user = await User.get_or_none(id=user_id)

    return await generate_html_response(
        name=user.call_name,
        age=user.age,
        count_user=await User.distinct_count()
    )
