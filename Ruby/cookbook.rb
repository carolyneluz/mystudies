INSERIR_RECEITA = 1
VISUALIZAR_RECEITAS = 2
BUSCAR_RECEITAS = 3
SAIR = 4

def bem_vindo()  
  puts "Bem-vindo ao Cookbook, sua rede social de receitas"
end

def menu()  
  puts "[#{INSERIR_RECEITA}] Cadastrar uma receita"
  puts "[#{VISUALIZAR_RECEITAS}] Ver todas as receitas"
  puts "[#{BUSCAR_RECEITAS}] Buscar receitas"
  puts "[#{SAIR}] Sair" 

  print "Escolha uma opção: "
  return gets.to_i
end

def inserir_receita()
  puts "Digite o nome da receita: "
  nome = gets.chomp
  puts "Digite o tipo da receita: "
  tipo = gets.chomp
  puts
  puts "Receita #{nome} cadastrada com sucesso!"
  puts
  return { nome: nome, tipo: tipo }
end

def imprimir_receitas(receitas)
  puts "====Receitas cadastradas===="
  receitas.each do |receita|
    puts "#{receita[:nome]} - #{receita[:tipo]}"
  end
  puts
  if receitas.empty?
    puts "Nenhuma receita cadastrada"
  end
end

def buscar_receitas(receitas)
  puts "Digite o nome da receita que deseja buscar: "
  nome_busca = gets.chomp
  puts "====Resultado da busca===="
  receitas_encontradas = receitas.select { |receita| receita[:nome].downcase.include?(nome_busca.downcase) }
  
  if receitas_encontradas.empty?
    puts "Nenhuma receita encontrada com o nome '#{nome_busca}'"
  else
    receitas_encontradas.each do |receita|
      puts "#{receita[:nome]} - #{receita[:tipo]}"
    end
  end
  puts
end

bem_vindo()

receitas = []

opcao = menu()

loop do 
  if opcao == INSERIR_RECEITA
    receitas << inserir_receita()
  elsif opcao == VISUALIZAR_RECEITAS
    imprimir_receitas(receitas)
  elsif opcao == BUSCAR_RECEITAS
    buscar_receitas(receitas)
  elsif opcao == SAIR
    break
  else 
    puts "Opção inválida"
  end

  opcao = menu()
end

puts
puts 'Obrigado por usar o Cookbook, até logo!'


opcao = menu()

while(opcao != 3) do 
  if(opcao == 1)
    receitas << inserir_receita()
  elsif(opcao == 2)
    imprimir_receitas(receitas)
  else 
    puts "Opção inválida"
  end

  opcao = menu()
end

puts 'Obrigado por usar o Cookbook, até logo!'