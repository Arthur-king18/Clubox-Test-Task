from backend.src.project.settings import settings

config = {
    'connections': {
        'default': f'postgres://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}'
                   f'@localhost:1338/{settings.POSTGRES_DB}'
    },
    'apps': {
        'models': {
            'models': ['backend.src.project.db.models', 'aerich.models'],
            'default_connection': 'default'
        }
    }
}
