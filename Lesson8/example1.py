import  logging
logging.basicConfig(level = logging.DEBUG, filename = "logs.log", filemode = "a",
                    format="%(asctime)s %(levelname)s - %(message)s" )
# напишіть функцію в середині якого буде наступний код а
# числа для ділення будуть передаватися аргуметрами функції
def div(a,b):
    try:
        print(a/b)
    except Exception:
        logging.exception(Exception)
div(2,3)
div(4,0)