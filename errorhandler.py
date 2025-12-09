# error_handler.py
from functools import wraps
import logging
import traceback

logger = logging.getLogger(__name__)

def handle_errors(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {f.__name__}: {str(e)}")
            logger.error(traceback.format_exc())
            return {
                'error': True,
                'message': "I apologize, but I'm having trouble processing that. Could you try rephrasing?"
            }
    return wrapper