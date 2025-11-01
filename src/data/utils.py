# src/data/utils.py
"""
Funções utilitárias para download e processamento de dados do projeto Hypnos Data
"""

import os


def get_output_path(filename="Sleep_Efficiency_Processed.csv", data_type="processed"):
    """
    Detecta o ambiente e retorna o caminho apropriado para salvar arquivos

    Args:
        filename (str): Nome do arquivo a ser salvo
        data_type (str): Tipo de dados ('processed', 'raw')

    Returns:
        str: Caminho completo para salvar o arquivo

    Examples:
        >>> output_path = get_output_path()
        >>> df.to_csv(output_path, index=False)
    """
    # Detectar se está no Google Colab
    try:
        import google.colab
        print("Ambiente: Google Colab")
        # No Colab, salva na pasta raiz
        return filename
    except ImportError:
        pass

    # Detectar se está no Kaggle
    if os.path.exists('/kaggle/working'):
        print("Ambiente: Kaggle")
        return f"/kaggle/working/{filename}"

    # Ambiente local (PyCharm, Jupyter, VSCode, etc.)
    print("Ambiente: Local")

    # Tenta encontrar a estrutura de pastas do projeto
    output_dir = os.path.join("..", "data", data_type)

    if os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        return os.path.join(output_dir, filename)
    else:
        # Fallback: salva no diretório atual
        print("Estrutura de pastas não encontrada. Salvando no diretório atual.")
        return filename


def get_input_path(filename="Sleep_Efficiency_Processed.csv", data_type="processed"):
    """
    Detecta o ambiente e retorna o caminho apropriado para carregar arquivos

    Args:
        filename (str): Nome do arquivo a ser carregado
        data_type (str): Tipo de dados ('processed', 'raw', 'interim')

    Returns:
        str: Caminho completo para carregar o arquivo

    Examples:
        >>> input_path = get_input_path()
        >>> df = pd.read_csv(input_path)
    """
    # Detectar se está no Google Colab
    try:
        import google.colab
        print("Ambiente: Google Colab")
        return filename
    except ImportError:
        pass

    # Detectar se está no Kaggle
    if os.path.exists('/kaggle/working'):
        print("Ambiente: Kaggle")
        return f"/kaggle/working/{filename}"

    # Ambiente local
    print("Ambiente: Local")

    # Tenta encontrar na estrutura de pastas do projeto
    input_path = os.path.join("..", "data", data_type, filename)

    if os.path.exists(input_path):
        return input_path
    else:
        # Fallback: busca no diretório atual
        print("Arquivo não encontrado na estrutura padrão. Buscando no diretório atual.")
        return filename
