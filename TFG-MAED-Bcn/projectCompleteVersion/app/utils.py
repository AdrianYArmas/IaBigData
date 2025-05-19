def creacion_atributos(df):
    df['dia_semana'] = df.index.dayofweek
    df['dia_año'] = df.index.dayofyear
    df['trimestre'] = df.index.quarter
    df['mes'] = df.index.month
    df['año'] = df.index.year
    return df