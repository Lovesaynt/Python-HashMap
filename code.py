class Hashmaps:
    def __init__(self, size=100):
        self.size = size # Recebe a quantidade de buckets.
        self.buckets  = [[] for _ in range(size)] # Gera os Buckets.


    def _hash(self, key): # Recebe o valor hash e calcula módulo qtd.buckets.
        return hash(key) % self.size # Ex: 534536346248 % 100.


    def put(self, key, value): # Insere a Chave e seu Valor dentro de um bucket.
        index = self._hash(key) # Calcula o index da chave x do bucket.
        bucket = self.buckets[index] # Determina a chave e seu valor ao bucket.

        for i, (k, v) in enumerate (bucket): # Enumera os buckets e busca K, V dentro deles.
            if k == key: # Se k'Chave' no bucket for igual ao parâmetro'chave' informado.
                bucket[i] = (key, value) # O bucket na indexagem [i] terá sua key e value substituídos
                return
        bucket.append((key,value)) # Atribui a chave e seu valor ao bucket.


    def get(self, key): # Retorna o valor da chave atribuída ao bucket.
        index = self._hash(key) # Calcula o index da chave x do bucket.
        bucket = self.buckets[index] # Determina a chave e seu valor ao bucket.

        for k, v in bucket: # Para cada chave e valor dentro dos buckets.
            if k == key: # Se k'Chave' no bucket for igual ao parâmetro'chave' informado.
                return v # Retorna o valor.
        raise KeyError('key') # Key não encontrada.


    def remove(self, key): # Remove o bucket indicado.
        index = self._hash(key) # Calcula o index da chave x do bucket.
        bucket = self.buckets[index] # Determina a chave e seu valor ao bucket.

        for i, (k, _) in enumerate(bucket): # Enumera os buckets e busca a key informada dentro deles.
            if k == key: # Se k'Chave' no bucket for igual ao parâmetro'chave' informado.
                del bucket[i] # Deleta o bucket na indexagem [i].
                return
        raise KeyError(key) # Key não encontrada.


    def debug(self, key): # Exibe detalhes importantes.
        index = self._hash(key) # Calcula o index da chave x do bucket.
        bucket = self.buckets[index] # Determina a chave e seu valor ao bucket.

        print('DEBUG') # Titulo
        print(f'Chave: {key}') # Chave
        print(f'Índice: {index}') # Indíce do Bucket
        print(f'Bucket: {bucket}') # Conteúdo do Bucket


    def show(self): # Exibe todos os buckets.
        for i, bucket in enumerate(self.buckets): # Para cada item no balde, enumere-os.
            print(f'{i}: {bucket}') # Exibe a indexagem, o balde e seu conteúdo.
