async def emergency_stop(update, context):
    await update.message.reply_text("🛑 Sistem dihentikan (manual trigger).")
    exit(0)
