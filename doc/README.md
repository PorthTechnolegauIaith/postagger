[scroll down for english](#pos-tagger-api)

# API Tagiwr Rhannau Ymadrodd

Mae'r API yn gweithio dros HTTPS GET, felly gellir defnyddio unrhyw iaith raglennu neu feddalwedd HTTP er mwyn cysylltu â'r API.

## Fersiwn Cyfredol

Un fersiwn o API Tagiwr Rhannau Ymadrodd sydd ar gael, sef v1 neu 'fersiwn 1'.
Mae'r fersiwn a ddefnyddwyd yn cael ei dychwelyd yn y canlyniadau JSON.

Bydd yr URL yn newid gyda phob fersiwn newydd o'r API. Ar hyn o bryd, dylid defnyddio `/v1` ar gyfer fersiwn 1.

## Sgema

Mae cysylltiad â'r API yn gweithio dros HTTPS yn unig, gan ddefnyddio'r parth `api.techiaith.org/pos`. Mae'r holl data sy'n cael eu derbyn/hanfon yn cael ei drosglwyddo ar ffurf JSON ([unicode-escaped ASCII](http://tools.ietf.org/html/rfc5137)).

## Paramedrau yr API

| Paramedr   | Disgrifiad | Sylwadau |
|------------|------------|----------|
| `api_key`  | Eich allwedd API, ar gael o'r Canolfan APIs (http://api.techiaith.org) | angenrheidiol |
| `text`     | Y testun i'w dagio. Dylid ei fformatio yn ôl RFC 3986 (percent-encoded) | angenrheidiol |
| `lang`     | Yr iaith ar gyfer unrhyw destun fydd yn cael ei ddychwelyd (e.e. negeseuon gwall). Dewis o `en` neu `cy`. Rhagosodiad: `cy` | dewisiol |
| `callback` | Enw 'function' ar gyfer unrhyw callback JSON-P (gweler isod) | dewisiol |

### Enghraifft

```
$ curl http://api.techiaith.org/pos/v1/?api_key=123&text=mae%20hen%20wlad%20fy%20nhadau

{
    "success": true,
    "result": "mae/VBF/- hen/ADJP/- wlad/NF/TM fy/PRONOUN/- nhadau/NPL/TT",
    "version": 1
}

```

## Canlyniadau

Mae'r canlyniadau mewn fformat:

```
gair/RHAN_YMADROD/TREIGLAD
```

Mae'r tablau isod yn rhestru ystyr pob byrfodd rhan ymadrodd/treiglad

**Byrfoddau Rhanau Ymadrodd**

| Byrfodd | Ystyr |
|-----------|-------|
| ABBR | talfyriad |
| ACRONYM | acronym |
| ADJ | ansoddair |
| ADJCOMP | ansoddair cymharol |
| ADJEQ | ansoddair cyfartal |
| ADJF | ansoddair benywaidd |
| ADJM | ansoddair gwrywaidd |
| ADJP | andosddair rhagddodol |
| ADJPL | ansoddair lluosog |
| ADJPO | anssoddair rhagddodol achlysurol |
| ADJQ | ansoddair goleddfydd |
| ADJQT | andoddair goleddfydd gyda treiglad |
| ADJSUP | ansoddair eithaf |
| ADV | adferf |
| ALPHNUM | nod alffaniwmerig |
| APSADJ | atodiad agweddol |
| ARALL | arall |
| CARD | rhifolyn |
| CARDF | rhifolyn benywaidd |
| CARDM | rhifolyn gwrywaidd |
| COMPWORD | gair cyfansawdd |
| CONJ | cysylltair |
| CPREP | arddodiad rhediadol |
| DEMPRON | rhagenw dangosiadol |
| DET | banod |
| ENGLISH | Saesneg |
| EOS | diwedd brawddeg |
| EXCLAM | ebych |
| FOREIGN | estron |
| IGNORE | anwybyddu (anwybyddir y gair gan y tagiwr) |
| INTPRON | rhagenw gofynnol |
| LEANRT | gair personol |
| LET | llythyren |
| ND | enw deuol |
| NF | enw benywaidd |
| NFPROP | enw priod benywaidd |
| NM | enw gwrywaidd |
| NMF | enw gwrywaidd benywaidd |
| NMPROP | enw priod gwrywaidd |
| NOUNCOLL | enw torfol |
| NPL | enw lluosog |
| NUMBER | rhif |
| ORD | trefnolyn |
| ORDF | trefnolyn benywaidd |
| ORDM | trefnolyn gwrywaidd |
| PARTITER | geiryn gofynnol |
| PARTNEG | geiryn negyddol |
| PARTPV | geiryn |
| PERSON | enw person |
| PLACE | enw lle |
| PREDYN | YN traethiadol  (e.e. `'n` yn `mae'n`) |
| PREFIX | rhagddodiad |
| PREP | arddodiad |
| PRONF | rhagenw benywaidd |
| PRONM | rhagenw gwrywaidd |
| PRONOUN | rhagenw |
| PRONPL | rhagenw lluosog |
| PRONREL | rhagenw perthynol |
| PUNCT | atalnod |
| REFUSE | gwrthod |
| RELPARTNEG | geiryn negyddol perthynol |
| ROMAN | rhif rhufeinig |
| VB | berf |
| VBF | ffurf ferfol |
| VERBADJ | atodiad berfol |
| VR | bon y ferf |
| ? | anhysbys |

**Byrfoddau Treigladau**

| Byrfodd | Ystyr |
|-----------|-------|
| TM | Treiglad Meddal |
| TL | Treiglad Llaes |
| TT | Treiglad Trwynol |
| TH | Treiglad Rhagddodiad (ychwanegu 'h' e.e. eu hiaith) |
| - | Dim Treiglad |
| ? | Anhysbys |

## JSON-P Callbacks

Gellir defnyddio'r API gyda JSON-P callbacks trwy ychwanegu'r paramedr `callback` i'ch galwad:

```
$ curl https://api.techiaith.org/pos/v1/?api_key=rhywbeth&text=mae hen wlad fy tadau&callback=foo
foo({
    "success": true,
    "version": 1,
    "result": "mae/VBF/- hen/ADJP/- wlad/NF/TM fy/PRONOUN/- nhadau/NPL/TT"
});
```


## Cyfyngu nifer yr alwadau yr awr

Mae gan yr API gyfyngiad ar nifer yr alwadau y gellir eu gwneud mewn awr.

Os ydych eisiau cynyddu nifer y galwadau sydd ar gael i chi drwy'r API, defnyddiwch y ffurflen yn y 'Canolfan APIs'

Gellir gweld cyfanswm nifer eich galwadau ar unrhyw adeg trwy edrych ar y 'HTTP headers' yn eich galwad API:

```
$ curl -i http://api.techiaith.org/pos/v1/?api_key=rhywbeth&text=un%20dau%20tri                                                            

HTTP/1.1 200 OK
Date: Mon, 17 Nov 2014 14:41:21 GMT
Content-Type: application/json
Content-Language: cy
X-Ratelimit-Remaining: 276
X-Ratelimit-Limit: 300
X-Ratelimit-Reset: 1416237399
```

Mae'r headers yn cynnwys yr holl wybodaeth sydd ei angen:

| Enw'r Header | Disgrifiad |
|--------------|------------|
| X-RateLimit-Limit | Nifer mwyaf o alwadau y gallwch chi eu gwneud mewn awr |
| X-RateLimit-Remaining | Nifer y galwadau sydd gennych chi ar ôl yn y 'blwch' cyfyngu presennol |
| X-RateLimit-Reset | Yr amser pryd bydd y 'blwch' cyfyngu presennol yn cael ei ail-osod, mewn [eiliadau epoch UTC](http://en.wikipedia.org/wiki/Unix_time) |

Os ydych chi angen yr amser mewn fformat gwahanol, gellir gwneud hyn gydag unrhyw iaith raglennu modern. Er engraifft, gellir gwneud hyn trwy gonsol eich porwr (gyda Javascript) a dychwelych gwrthrych 'Javascript Date'.

```javascript
new Date(1416237399 * 1000)
Date 2014-11-17T15:16:39.000Z
```

Ar ôl i chi fynd dros eich nifer mwyaf o alwadau yr awr, byddwch yn derbyn gwall gan y gweinydd (403 Forbidden):

```
curl -i http://api.techiaith.org/pos/v1/?api_key=123&text=mae%20hen%20gwlad%20fy%20tadau

HTTP/1.1 200 OK
Date: Tue, 18 Nov 2014 10:45:10 GMT
Content-Type: application/json
X-Ratelimit-Limit: 300
X-Ratelimit-Remaining: 0
Content-Language: cy
X-Ratelimit-Reset: 1416310586

{
    "success": false,
    "errors": ["403 Forbidden: Rydych chi wedi mynd dros eich cyfyngiad nifer yr alwadau yr awr"]
}
```

-----------------------

## POS Tagger API

The API works using HTTPS GET, meaning you can use it with any programming language/software package of your choice which works over HTTP

## Current Version

Currently, there is only one version of the POS Tagger API available: v1 or 'version 1'.
The version used for the request is returned in the JSON result.

## Schema

The connection to the API is over HTTPS only, from the domain `api.techiaith.org/pos`. All data sent to and received from the API is in JSON ([unicode-escaped ASCII](http://tools.ietf.org/html/rfc5137))

## API Parameters

| Parameter   | Description | Notes |
|------------|------------|----------|
| `api_key`  | Your API key, from the API Centre (http://api.techiaith.org) | required |
| `text`     | The text to POS tag. Formatted according to RFC 3986 (percent-encoded) | required |
| `lang`     | The language for any feedback text returned by the API (e.e. error messages). Choices: `en` or `cy`. Default: `cy` | optional |
| `callback` | Name of the function to wrap the response in for a JSON-P callback (see below) | optional |

### Example

```
$ curl http://pos.api.techiaith.org/v1/?api_key=123&text=mae%20hen%20wlad%20fy%20nhadau

{
    "success": true,
    "result": "mae/VBF/- hen/ADJP/- wlad/NF/TM fy/PRONOUN/- nhadau/NPL/TT",
    "version": 1
}

```

## Results

The API returns a string where each word in the sent text is tagged in the following format:

```
word/PART_OF_SPEECH/MUTATION
```

The tables below show the meanings of each abbreviation of the POS/mutation returned by the API

**POS Abbreviations**

| Abbreviation | Meaning |
|-----------|-------|
| ABBR | abbreviation |
| ACRONYM | acronym |
| ADJ | adjective |
| ADJCOMP | adjective comparative |
| ADJEQ | adjective equative |
| ADJF | adjective feiminine |
| ADJM | adjective masculine |
| ADJP | adjective prefix |
| ADJPL | adjective plural |
| ADJPO | adjective prefix occasional |
| ADJQ | adjective qualifier |
| ADJQT | adjective qualifier with mutation |
| ADJSUP | adjective superlative |
| ADV | adverb |
| ALPHNUM | alphanumeric character |
| APSADJ | aspective adjuct |
| ARALL | other |
| CARD | cardinal |
| CARDF |  cardinal feminine |
| CARDM | cardinal masculine |
| COMPWORD | compound word |
| CONJ | conjunct |
| CPREP | conjugative preposition |
| DEMPRON | demonstrative pronoun |
| DET | determiner |
| ENGLISH | english |
| EOS | end of sentence |
| EXCLAM | exclamation |
| FOREIGN | foreign |
| IGNORE | ignore (this word is ignored by the POS tagger) |
| INTPRON | interrogative pronoun |
| LEANRT | personal word |
| LET | letter |
| ND | noun double |
| NF | noun feminine |
| NFPROP | proper noun feminine |
| NM | noun masculine |
| NMF | noun masculine feminine |
| NMPROP | proper noun masculine |
| NOUNCOLL | noun collective |
| NPL | noun plural |
| NUMBER | number |
| ORD | ordinal |
| ORDF | ordinal feminine |
| ORDM | ordinal masculine |
| PARTITER | interrogative particle |
| PARTNEG | negative particle |
| PARTPV | particle |
| PERSON | person name |
| PLACE | place name |
| PREDYN | YN predicative (e.g. `'n` in `mae'n`)|
| PREFIX | prefix |
| PREP | preposition |
| PRONF | pronoun feminine |
| PRONM | pronoun masculine |
| PRONOUN | pronoun |
| PRONPL | pronoun plural |
| PRONREL | relative pronoun |
| PUNCT | punctuation |
| REFUSE | refuse to tag |
| RELPARTNEG | relative negative particle |
| ROMAN | roman numeral |
| VB | verb |
| VBF | verbal form |
| VERBADJ | verbal adjunct |
| VR | verb root |
| ? | unknown |

**Mutation Abbreviations**

| Talfyriad | Ystyr |
|-----------|-------|
| TM | Soft Mutation |
| TL | Asparite Mutation |
| TT | Nasal Mutation |
| TH | Prefix Mutation (addition of 'h' e.g. eu hiaith) |
| - | No Mutation |
| ? | Unknown |

## JSON-P Callbacks

You can use the API with JSON-P callbacks by adding the parameter `callback` to your request:

```
$ curl https://api.techiaith.org/pos/v1/?api_key=rhywbeth&text=mae hen wlad fy tadau&callback=foo
foo({
    "success": true,
    "version": 1,
    "result": "mae/VBF/- hen/ADJP/- wlad/NF/TM fy/PRONOUN/- nhadau/NPL/TT"
});
```


## Rate Limiting

The API has a limit on the number of requests you can make per hour, linked to your API key.

If you would like to increase the number of requests you can make to the API per hour, use the form within the 'API Centre'.

You can view the number of requests you have made/have remaining at any time by looking at the 'HTTP headers' of any response to the API:

```
$ curl -i http://api.techiaith.org/pos/v1/?api_key=rhywbeth&text=un%20dau%20tri                                                            

HTTP/1.1 200 OK
Date: Mon, 17 Nov 2014 14:41:21 GMT
Content-Type: application/json
Content-Language: cy
X-Ratelimit-Remaining: 276
X-Ratelimit-Limit: 300
X-Ratelimit-Reset: 1416237399
```

The headers contain all information you may require:

| Header Name | Description |
|--------------|------------|
| X-RateLimit-Limit | Maximum number of requests you can make per hour (rate limit) |
| X-RateLimit-Remaining | The number of requests remaining in the current rate limit window |
| X-RateLimit-Reset | The time at which the current rate limit window resets in [UTC epoch seconds](http://en.wikipedia.org/wiki/Unix_time) |


If you need the time in a different format, any modern programming language can get the job done. For example, if you open up the console on your web browser, you can easily get the reset time as a JavaScript Date object.

```javascript
new Date(1416237399 * 1000)
Date 2014-11-17T15:16:39.000Z
```

Once you go over the rate limit you will receive an error response:

```
$ curl -i http://api.techiaith.org/pos/v1/?api_key=123&text=mae%20hen%20gwlad%20fy%20tadau&lang=en

HTTP/1.1 200 OK
Date: Tue, 18 Nov 2014 10:44:37 GMT
Content-Type: application/json
X-Ratelimit-Limit: 300
X-Ratelimit-Remaining: 0
Content-Language: en
X-Ratelimit-Reset: 1416310586

{
    "success": false,
    "errors": ["403 Forbidden: You have exceeded your request limit"]
}
```
