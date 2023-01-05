# Project faker

Als eindproject voor api heb ik gekozen om verder te werken aan mijn basis faker project. In het basis project kon de gebruiker zijn naam opgeven en een willekeurige japanse of amerikaanse naam terugkrijgen. In dit project breiden we dit uit, de gebruiker moet zich registreren hierna kan hij een amerikaanse of japanse naam genereren. inloggen is ook een mogelijkheid dit is nodig om de beveiligde functies te gebruiken zoals namen bekijken, aanpassen en verwijderen.

dit is nodig om de gebruikers en random namen te bekijken omdat de gebruiker geauthorizeerd moet zijn. 

> POST "/user" Hiermee kan je een gebruiker aanmaken die je later kunt gebruiken om de token op te vragen.<br>
> GET "/users" Dit geeft een lijst van alle gebruikers weer.<br>
> GET "/users/{user_id}" Hiermee kan je van een bepaalde gebruiker (via de ownerid) gegevens opvragen.<br>
> GET "/america" Hiermee kan je de gegenereerde amerikaanse namen zien<br>
> POST "/america" Hiermee kan je een amerikaanse naam genereren op owner-id.<br>
> GET "/japan" Hiermee kan je de gegenereerde japanse namen zien.<br>
> POST "/japan" Hiermee kan je een japanse naam genereren op owner-id.<br>
> POST "/token" Hiermee kan je een token opvragen via de user inloggegevens, deze token kan je gebruiken om beveiligde requests te doen.<br>
> PUT "/users/{username}" Hiermee kan je een gebruikersnaam aanpassen.<br>
> DELETE "/users/{username}" Hiermee kan je een gebruiker verwijderen.<br>

## Links
* API Links
    * [API Repository](https://github.com/CisseM03/end-api)
    * [Hosted API](https://api-eindproject-cissem03.cloud.okteto.net)
   
Alle algemene eisen zijn behaald
     
## Eigen Aanvullingen 
   * Meer endpoints dan nodig

## Postman (API Testing)
> POST "/user" Hiermee kan je een gebruiker aanmaken die je later kunt gebruiken om de token op te vragen.
![image](https://i.imgur.com/f8R36QU.png)

> GET "/users" Dit geeft een lijst van alle gebruikers weer.<br>
![image](https://i.imgur.com/5Xip0Sr.png)

> GET "/users" wanneer niet geauthenticeerd.<br>
![image](https://i.imgur.com/e5xBiK7.png)

> GET "/users/{user_id}" Hiermee kan je van een bepaalde gebruiker (via de ownerid) gegevens opvragen.<br>
![image](https://i.imgur.com/jwpa03N.png)

> GET "/america" Hiermee kan je de gegenereerde amerikaanse namen zien<br>
![image](https://i.imgur.com/Ev3kKrO.png)

> POST "/america" Hiermee kan je een amerikaanse naam genereren op owner-id.<br>
![image](https://i.imgur.com/8RzZ9Uc.png)

> GET "/japan" Hiermee kan je de gegenereerde japanse namen zien.<br>
![image](https://i.imgur.com/D8xHslX.png)

> POST "/japan" Hiermee kan je een japanse naam genereren op owner-id.<br>
![image](https://i.imgur.com/mPQ1Nao.png)

> POST "/token" Hiermee kan je een token opvragen via de user inloggegevens, deze token kan je gebruiken om beveiligde requests te doen.<br>
![image](https://i.imgur.com/watj2B3.png)

>![image](https://i.imgur.com/lGV48Bc.png)

> PUT "/users/{username}" Hiermee kan je een gebruikersnaam aanpassen.<br>
![image](https://i.imgur.com/vmVMKAS.png)

> DELETE "/users/{username}" Hiermee kan je een gebruiker verwijderen.<br>
![image](https://i.imgur.com/vWB5n1u.png)

## OpenAPI Docs Screenshots
![image](https://i.imgur.com/BK8NnVw.png)

