from __future__ import annotations

from CNB_application import create_app
from CNB_application.core import logger

app = create_app()

if __name__ == '__main__':
    logger.info('Starting CNB API ...')
    app.run(
        host='0.0.0.0',
        port=5000,
        threaded=True,
        ssl_context=('certs/localhost.pem', 'certs/localhost-key.pem'),
    )
    logger.info('End of CNB App')
