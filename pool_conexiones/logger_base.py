import logging

logger = logging
logger.basicConfig(level=logging.DEBUG,
                   format= '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)s]: %(message)s', 
                   handlers=[ 
                        logging.FileHandler('capa_datos.log'),
                        logging.StreamHandler()
                    ])

if __name__=='__main__':
    logger.warning('Watch out!')  # will print a message to the console
    logger.info('I told you so')  # will not print anything
    logger.debug('debug impresio')

