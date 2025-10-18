import random as r

class Team: 
    def __init__(self, name, matches = 0):
        self.name = name
        self.__wins = 0
        self.__loses = 0
        self.__ties = 0
        self.__matches_played = 0
        self.__goals_for = 0 # A favor
        self.__goals_against = 0 # En contra
        self.__pnts = 0
        
    def register_match(self, goals_scored, goals_conceded):
        """
        goals_scored = Goles que el equipo anotó
        goals_conceded = Goles en contra.
        """
        self.__matches_played += 1
        self.__goals_for += goals_scored        # + Goles a favor
        self.__goals_against += goals_conceded  # + Goles en contra
        
        # Asigna victoria/derrota o empate dependiendo 
        # de los goles de la partida jugoals_concededda.
        if goals_scored > goals_conceded:
            self.__wins += 1
            self.__pnts += 3
        elif goals_scored < goals_conceded:
            self.__loses += 1
            # no hay puntos :c
        else:
            self.__ties += 1
            self.__pnts += 1

        return f"Actualización de estadísticas completadas para {self.name}!" 
        
    def goals_difference(self):
        return self.__goals_for - self.__goals_against
    
    # Metodos getter
    def get_wins(self):
        return self.__wins

    def get_loses(self):
        return self.__loses

    def get_ties(self):
        return self.__ties
    
    def get_goals_for(self):
        return self.__goals_for
    
    def get_goals_against(self):
        return self.__goals_against

    def get_points(self):
        return self.__pnts

    def get_matches_played(self):
        return self.__matches_played

class Match:
    def __init__(self, local_team, away_team, local_goals = 0, away_goals = 0):
        self.local_team: Team = local_team
        self.away_team: Team = away_team
        self.local_goals = local_goals  # Comienza en 0 cada partido al principio
        self.away_goals = away_goals    # Esto no deberia de ser un atributo de instancia lol

    def play_match(self):
        # Genera goles aleatorios por cada equipo
        local_goals = r.randint(0, 5)
        away_goals = r.randint(0, 5)

        # Se registra el partido para cada equipo
        self.local_team.register_match(local_goals, away_goals)
        self.away_team.register_match(away_goals, local_goals)

class Tournament:
    def __init__(self, teams=[]):
        self.__teams = teams
        self.__matches = []
    
    def add_team(self, new_team):
        self.__teams.append(new_team)
        
    def simulate_tournament(self):
        """
        Genera todas las rondas de ida y vuelta para cada equipo.
        """
        print(f"Generando partidos para {len(self.__teams)} equipos...")
        print("Lista partidos:")
        
        for i in range(len(self.__teams)):
            for j in range(len(self.__teams)):
                if i != j: # Prevenir partidos duplicados. Evita equipo1 vs equipo1.
                    home_team = self.__teams[i]
                    away_team = self.__teams[j]
                    
                    match = Match(home_team, away_team)
                    match.play_match() # Se registra el partido actual para cada equipo
                    self.__matches.append(match)
                    
                    print(f"   {len(self.__matches)}. {home_team.name} vs {away_team.name}")
        
        print(f"Total de partidos generados: {len(self.__matches)}")

    def table(self):
        # Se utiliza una función anonima para especificar el atributo de la clase para sortear
        sorted_teams = sorted(self.__teams, key=lambda lol: lol.get_points(), reverse=True)

        print("\n🏆 TABLA DE POSICIONES")
        print("-" * 50)
        print("Pos Equipo\t\tPJ W  L  T  GF  GC  DG  Pts")
        for i, team in enumerate(sorted_teams):
            print(f" {i+1}  {team.name}\t\t{team.get_matches_played()}  "
                  f"{team.get_wins()}  {team.get_loses()}  {team.get_ties()}  "
                  f"{team.get_goals_for()}  {team.get_goals_against()}  "
                  f"{team.goals_difference()}   {team.get_points()}")

# Creación de los 4 equipos clasificados
liverpool = Team('Liverpool')
madrid = Team('Real Madrid')
barca = Team('Barcelona')
juventus = Team('Juventus')

# Lista de equipos anteriormente creados
teams = [liverpool, madrid, barca, juventus]

# Crear torneo
final = Tournament(teams)
final.simulate_tournament()
final.table()