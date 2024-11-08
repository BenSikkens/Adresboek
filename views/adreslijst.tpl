%include('header.tpl', Title='Adressen')

<main>

  <section class="left">
    %include('navi.tpl')
  </section>
  <section class="right">
    <h2>Adressenlijst</h2>
    <p>
      <ul style="list-style-type:none">
        %for col in nawdata:
        <li>id: {{col['id']}}</li>
        <li>Naam: {{col['voornaam']}} {{col['prefix']}} {{col['achternaam']}} </li>
        <li>Adres: {{col['straatnaam']}} {{col['huisnummer']}} {{col['postcode']}} {{col['plaatsnaam']}}</li>
        <li><br></li>
        %end
      </ul>
	</p>
  </section>
</main>

%include('footer.tpl')