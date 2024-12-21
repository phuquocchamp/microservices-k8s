import pika, json, logging

# Configure logging
logger = logging.getLogger(__name__)

def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
        logger.info(f"File uploaded successfully with fid: {fid}")
    except Exception as err:
        logger.error(f"Failed to upload file: {err}")
        return None, 500  # Hoặc đơn giản là return 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access.get("username"),  # Sử dụng .get() để tránh KeyError
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        logger.info(f"Message published successfully: {message}")
    except Exception as err:
        logger.error(f"Failed to publish message: {err}")
        try:
            fs.delete(fid)
            logger.info(f"Successfully deleted file with fid: {fid} after message publishing failure")
        except Exception as delete_err:
            logger.error(f"Failed to delete file with fid: {fid}: {delete_err}")
        return None, 500  # Hoặc đơn giản là return 500