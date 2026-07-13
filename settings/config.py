# Just separate databases to test
POSTGRES_11 = "postgresql+psycopg2://username:password@host:port/sqlalchemy_11"  # 1:1
POSTGRES_1N = "postgresql+psycopg2://username:password@host:port/sqlalchemy_1n"  # 1:N
POSTGRES_NN = "postgresql+psycopg2://username:password@host:port/sqlalchemy_nn"  # N:N
