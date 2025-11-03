from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Configurações do Alembic (.ini)
config = context.config

# Carrega logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa os models e o Base
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # adiciona a pasta principal no path

from src.settings.database import Base, settings  # importa o Base e o settings
from src.models.Alunos import Alunos
from src.models.Disciplina import Disciplina
from src.models.Matricula import Matricula
from src.models.Nota import Nota
from src.models.Frequencia import Frequencia
from src.models.Professor import Professor

# Define o metadata que o Alembic vai usar
target_metadata = Base.metadata

# Define a URL do banco de dados
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

def run_migrations_offline() -> None:
    """Executa migrações no modo offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa migrações no modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
