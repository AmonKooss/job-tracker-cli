import database as db

status_vagas = ['salva','aplicada','entrevista','rejeitada']#lista de possibilidades de status de uma vaga
possiblidades = range(1,7) #aqui criei uma lista dos valores de possiblidades do menu só pra ficar mais fácil 

#função que mostra as escolhas disponíveis do menu
def escolhas():
  print('\t GERENCIAMENTO DE VAGAS\n')
  print('-'*40)
  print('1 - Adicionar vaga')
  print('2 - Listar vagas')
  print('3 - Remover vaga')
  print('4 - Buscar vaga por status')
  print('5 - Atualizar status')
  print('6 - Sair')
  print('\n')

#Aqui a função para adicionar vaga no nosso banco de dados, puxando os dados informados pelo usuário 1ª opção
def add_vaga(empresa,cargo,link=' ',status= 'salva'):
  db.curr.execute(
    "INSERT INTO vagas (empresa, cargo, link, status) VALUES (?, ?, ?, ?)",
    (empresa, cargo, link, status)
  )
  db.conexão.commit() 
  id_criado = db.curr.lastrowid
  print(f'Vaga adicionada com ID {id_criado}')
  print('Vaga criada com sucesso')
  print('\n')

#Função que basicamente lista todas as vagas presentes 2ª opção
def listar_vagas():
  db.curr.execute('SELECT * FROM vagas ')
  itens = db.curr.fetchall()
  print(f"{'ID':<5} {'Empresa':<15} {'Cargo':<20} {'Link':<20} {'Status':<10}")
  print("-"*80)

  if not itens:
    print("Nenhuma vaga cadastrada.")
    return

  for id, empresa, cargo, link, status in itens:
    print(f"{id} | {empresa} | {cargo} | {link} | {status}")  

  print('\n')

#Função para remover uma vaga através do ID informado pelo usuário 3ª opção
def remover_vaga(id):
  db.curr.execute('DELETE FROM vagas WHERE id = ?',(id,))
  db.conexão.commit()
  print('\n')
  

# Função para buscar vaga por status (salva, aplicada, entrevista,rejeitada) 4ª opção
def busca_vaga(status='salva'):
  db.curr.execute('SELECT * FROM vagas WHERE status = ?',(status,))
  itens = db.curr.fetchall()
  print(f"{'ID':<5} {'Empresa':<15} {'Cargo':<20} {'Link':<20} {'Status':<10}")
  print("-"*80)

  if not itens:
    print("Nenhuma vaga encontrada com esse status.")
    return
  
  for id, empresa, cargo, link, status in itens:
    print(f"{id} | {empresa} | {cargo} | {link} | {status}")
  print('\n')
  

#Função para atualizar o status de uma vaga 5ª opção
def atualizar(id,status='aplicada'):
  db.curr.execute('UPDATE vagas SET status = ? WHERE id = ?',(status,id))
  db.conexão.commit()
  
  print('Status da vaga atualizado com sucesso ')
  print('\n')

def menu():
  while(True):
    escolhas()
    try:
        opt = int(input('Informe sua opção desejada: '))
        while(opt not in possiblidades):
          print('[ERRO] Valor inválido!')
          opt = int(input('Informe sua opção desejada: '))
      
        match opt:
            case 1:
                empresa = str(input('Empresa: '))
                cargo = str(input('Cargo: '))
                link = str(input('Link: '))
                status = input('Status: ')
                while status not in status_vagas:
                    print('[ERRO] Status inválido!')
                    status = input('Status: ')

                add_vaga(empresa,cargo,link,status)                

            case 2:
                listar_vagas()
                
            case 3:
              id = int(input('Informe o ID da vaga que deseja remover: '))
              remover_vaga(id)

            case 4:
              status =str(input('Informe o status da vaga: '))
              while(status not in status_vagas):
                print('[ERRO] Valor inválido!')
                status =str(input('Informe o status da vaga: '))
              busca_vaga(status)

            case 5:
              id = int(input('Informe o ID da vaga que deseja atualizar o status: '))
              status = str(input('Digite o novo status dessa vaga: '))
              while(status not in status_vagas):
                print('[ERRO] Valor inválido!')
                status = str(input('Digite o novo status dessa vaga: '))
              
              atualizar(id,status)

            case 6:
              db.conexão.close()
              print('Saindo...')
              break
          
    except ValueError:
      print('\033[1,31m[ERRO]Valor informado inválido![m')
      continue

