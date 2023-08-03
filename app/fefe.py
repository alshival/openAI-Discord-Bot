from app.config import *
from app.bot_functions import *
from app.keras import tasks_layer

# For creating reminders
from app.reminders.fefe_reminders_openai import *
# For general discussion
from app.fefe_openai import *
# For searching youtube
from app.fefe_youtube import *
from app.stocks import fefe_stock

async def talk_to_fefe(ctx, message,bot):

    model = "gpt-3.5-turbo"
    
    db_conn = await create_connection()
    username = ctx.author.name
    
    channel_name = ctx.channel.name,
    channel_id = ctx.channel.id
    try:
        message_category = await tasks_layer.classify_prompt(message)
        message_classified =True
    except Exception as e:
        # Capture the error message
        error_message = str(e)
        print(error_message)
        print(type(message))
        print(message)
        await ctx.send(f"""
        I'll need a bit more training to answer your question. You'll need to label your last prompt:
        {feature_display_text} 
        Then run `!retrain_keras`.
        """)
        await store_prompt(db_conn, ctx.author.name, message, model,'', channel_id,channel_name,keras_classified_as = 'ERROR')
        return

    # bot's Reminder Capabilities
    # if message_category == 'reminder':
    #     await reminder(ctx,message,model,db_conn)
    # # Bot's openAi capabilities
    # elif message_category == 'other':
    #     await fefe_openai(ctx,message,model,db_conn)
    # # Bot's youtube capabilities
    # elif message_category == 'youtube':
    #     await fefe_youtube(bot,ctx,message,model,db_conn)
    # elif message_category == 'interpreter':
    #     await fefe_stock.stock(ctx,message,model,db_conn)
    await fefe_stock.stock(ctx,message,model,db_conn)