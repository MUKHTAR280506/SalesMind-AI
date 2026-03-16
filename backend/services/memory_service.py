from app.database import SessionLocal
from app.models import Chat_history

def save_chat(session_id , user_msg, bot_msg):
    
    db = SessionLocal()

    chat = Chat_history (
        
        session_id = session_id,
        user_message = user_msg,
        bot_response = bot_msg
    )
   
    db.add(chat)
    db.commit()
    db.close()


def get_recent_context(session_id , limit=5):

    db= SessionLocal()

    chats = (                   # here () is used for multi line query format
        db.query(Chat_history) 
        .filter(Chat_history.session_id== session_id)
        .order_by(Chat_history.created_at.desc())
        .limit(limit)
        .all()
    )

    return chats