import os

async def set_pair(update, context):
    try:
        new_pair = context.args[0].upper()
        with open(".env", "r") as f:
            lines = f.readlines()
        with open(".env", "w") as f:
            for line in lines:
                if line.startswith("ACTIVE_PAIR="):
                    f.write(f"ACTIVE_PAIR={new_pair}\n")
                else:
                    f.write(line)
        await update.message.reply_text(f"✅ Pair diubah ke {new_pair}. Restart sistem untuk efek.")
    except:
        await update.message.reply_text("⚠️ Format salah. Contoh: /set_pair ETHUSDT")
