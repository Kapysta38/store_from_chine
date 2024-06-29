from .start import StartHandler
from .register import RegisterHandler
from .info import InfoHandler
from .order import OrderHandler, AcceptOrderHandler, DeclineOrderHandler
from .feedback import FeedbackHandler, FeedbackAnswerHandler

LIST_HANDLERS = [StartHandler, RegisterHandler, InfoHandler, OrderHandler, AcceptOrderHandler, DeclineOrderHandler,
                 FeedbackHandler, FeedbackAnswerHandler]
