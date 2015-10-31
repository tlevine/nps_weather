winter.parks <- c('http://www.nps.gov/alfl/planyourvisit/weather.htm',
                  'http://www.nps.gov/amis/planyourvisit/weather.htm',
                  'http://www.nps.gov/bibe/planyourvisit/weather.htm',
                  'http://www.nps.gov/bicy/planyourvisit/weather.htm',
                  'http://www.nps.gov/bith/planyourvisit/weather.htm',
                  'http://www.nps.gov/cabr/planyourvisit/weather.htm',
                  'http://www.nps.gov/cana/planyourvisit/weather.htm',
                  'http://www.nps.gov/chis/planyourvisit/weather.htm',
                  'http://www.nps.gov/chat/planyourvisit/weather.htm',
                  'http://www.nps.gov/chic/planyourvisit/weather.htm',
                  'http://www.nps.gov/ciro/planyourvisit/weather.htm',
                  'http://www.nps.gov/cong/planyourvisit/weather.htm',
                  'http://www.nps.gov/cuga/planyourvisit/weather.htm',
                  'http://www.nps.gov/deva/planyourvisit/weather.htm',
                  'http://www.nps.gov/ebla/planyourvisit/weather.htm',
                  'http://www.nps.gov/euon/planyourvisit/weather.htm',
                  'http://www.nps.gov/fopu/planyourvisit/weather.htm',
                  'http://www.nps.gov/gicl/planyourvisit/weather.htm',
                  'http://www.nps.gov/jica/planyourvisit/weather.htm',
                  'http://www.nps.gov/joda/planyourvisit/weather.htm',
                  'http://www.nps.gov/jomu/planyourvisit/weather.htm',
                  'http://www.nps.gov/lake/planyourvisit/weather.htm',
                  'http://www.nps.gov/lewi/planyourvisit/weather.htm',
                  'http://www.nps.gov/lyjo/planyourvisit/weather.htm',
                  'http://www.nps.gov/mawa/planyourvisit/weather.htm',
                  'http://www.nps.gov/manz/planyourvisit/weather.htm',
                  'http://www.nps.gov/malu/planyourvisit/weather.htm',
                  'http://www.nps.gov/orpi/planyourvisit/weather.htm',
                  'http://www.nps.gov/pais/planyourvisit/weather.htm',
                  'http://www.nps.gov/pinn/planyourvisit/weather.htm',
                  'http://www.nps.gov/redw/planyourvisit/weather.htm',
                  'http://www.nps.gov/rigr/planyourvisit/weather.htm',
                  'http://www.nps.gov/sagu/planyourvisit/weather.htm',
                  'http://www.nps.gov/sajh/planyourvisit/weather.htm',
                  'http://www.nps.gov/seki/planyourvisit/weather.htm',
                  'http://www.nps.gov/tapr/planyourvisit/weather.htm',
                  'http://www.nps.gov/tont/planyourvisit/weather.htm')

weather <- read.csv('weather.csv', stringsAsFactors = FALSE)
winter <- subset(weather, url %in% winter.parks)

by.state <- winter[order(winter$state), c('state', 'name', 'url')]

write.csv(by.state, file = 'winter.csv', row.names = FALSE)
