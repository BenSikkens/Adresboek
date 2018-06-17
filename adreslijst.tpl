<html>
  <head>
     <title>Adresboek</title>
     <link href="/css/main.css" rel="stylesheet">
  </head>
  <body>
      <h2>Adressenlijst</h2>
      <p>
      <ul style="list-style-type:none">
        %for col in nawdata:
        <li>id: {{col['id']}}
	    <li>Naam: {{col['voornaam']}} {{col['prefix']}} {{col['achternaam']}} </li>
	    <li>Adres: {{col['straatnaam']}} {{col['huisnummer']}} {{col['postcode']}} {{col['plaatsnaam']}}</li>
	    <li><br></li>
	    %end
	  </ul>
	  </p>
  </body>
</html>