# Český lorem ipsum generátor

Tento generátor byl vytvořen v rámci projektu v předmětu Programování ve 3. ročníku na SPŠEOL. Jedná se o generátor textu inspirovaný českým jazykem. Generátor jistě využijete v případě, kdyby Vás již nebavil klasický lorem ipsum text. Případně v situaci, ve které byste potřebovali generovat text s diakritikou. Například kdybyste vytvářeli textový font, který se bude používat na české texty.

## Jak generátor spustím?

1) Stáhnětě si ZIP z repozitáře na GitHubu.

2) Tento ZIP si extrahujte do Vámi zvolené složky.

3) Zdrojový kód generátoru se jmenuje: lorem_ipsum_generator.py

4) Stáhněte/Spustťe si program, ve kterém můžete kód spusit a zadat svůj vstup. Popřípadě si kód můžete vyzkošet v nějakém online prostředí skrze internetové připojení.

5) V případě chyby doinstalujte potřebná rozšíření či knihovny.

## Co dál?

Při spuštění zadejte, kolik vět chcete vygenerovat. Vygenerovaný text by se Vám měl zobrazit skrze textový dokument, který by se měl nacházet ve složce se samotným kódem. Textový dokument začíná hláškou o počtu vět, tu můžete víceméně ignorovat. Náhodně vytvořený text můžete zkopírovat a poté volně používat do všech vašich aplikací. V případě komplikací si můžete odkomentovat jeden z posledních řádků ve zdrojovém kódu (*Je nad ním komentář a sám je zakomentovaný*) a text si nechat vypsat do konzole.

> [!TIP]
> Některé parametry si v rámci kódu můžete upravit podle vašich potřeb. Vše je označeno komentářem.

> [!CAUTION]
> Vstup zadávejte číslicí, nikoliv slovně. Program by jinak nefungoval správně.

> [!NOTE]
> Příklad výstupního textového souboru s vygenerovaným textem Vám zde přikládám společně se zdrojovým kódem.

## Cíl projektu

Cílem projektu bylo vytvořit funkční generátor textu za pomocí základních a středně-pokročilých funkcí Pythonu. Znalosti, které jsem získal v hodinách, jsem poté aplikovat na vytvoření funkčního a spolehlivého kódu.

## Jak generátor funguje / Jak jsem nad jeho tvorbou přemýšlel

### Vstup od uživatele

Uživatel zadává, **kolik vět** bude chtít vygenerovat.

### Generování slov

Generátor funguje na tvorbě **podstatných jmen** a **sloves**. Všechna tyto slova se tvoří kombinováním ***předpon*** a ***přípon***, popřípadě ***koncovek***. Základem všeho jsou samozřejmě ***kořeny***.

**Předpony**, **přípony** a **koncovky** si program bere již z vytvořených seznamů. Volí si je náhodně, popřípadě si je nevolí vůbec.

Tvorba ***kořenů*** funguje na principu kombinování **samohlásek** a **souhlásek**, které si program bere také z již připravených seznamů. Počet kombinací je náhodný, rozsahově samozřejmě do určité míry omezený.

**Koncovky sloves** mají také svůj vlastní seznam, ale není to jediný způsob, jakým sloveso může končit...

Program si z určitého rozsahu zvolí náhodně počet podstatných jmen a sloves. Ty se uloží ***do seznamů***.

### Skládání samotných vět

Určitý počet podstatných jmen a sloves program postupně vkládá do vět. 

Při tvorbě těchto vět se také využívá dalších seznamů: seznam na **spojky (rozdělení vět)**, dále seznamy se **slovní vatou** a **citoslovci**.

Tyto prvky program náhodně vkládá postupně za sebe. Sekvence se ukončí ve chvíli, kdy jsou seznamy podstatných jmen a sloves prázdné.

Program si poté náhodně vybere **interpunkci**, pomocí které větu ukončí.

Část programu se také věnuje organizováním velkých písmen na začátku věty a také správě mezer.

### Zkompletování celého textu

Text se skládá z jednotlivých vět.

Je zde také část kódu, díky které se text vypíše do textového dokumentu.

Společně s tímto je tu i poměrně jednoduchá logika pro vypsání úvodní hlášky.

### Poznámky

Některé seznamy, ze kterých se skládají jednotlivá slova jsem měl rozsáhlejší. Po nějakém zhodnocení generovaných slov jsem se ovšem některé prvky rozhodl promazat, takže se seznamy mírně zúžily. Promazané prvky nejsou moc běžné a výstup se kvůli nim od češtiny spíše vzdaloval...

V programu mám také logiku, která po určitých příponách již negeneruje koncovky. Přípony jsou natolik zavedené, že se zde koncovky nehodí.

Také jsem zde řešil přílišný výskyt dvou samohlásek vedle sebe, což je jev, který pro češtinu není příliš přirozený. Toto jsem vyřešil vhodným generováním souhlásek v částech, kde to bylo zapotřebí.

## Jak by šel program zlepšit?

Určitě mě napadá nějaké vybírání jednotlivých částí slov podle četnosti v jazyce.

Dále také ošetření toho, aby se určitá písmena nedostala vedle sebe, popřípadě jen velmi zřídka.

Délka generovaných slov by se také mohla pohybovat v nějakých průměrných mezích daných českým jazykem. S tím, že by byla do kódu promítnuta nějaká adekvátní míra extrémů.

Uživatel by samozřejmě mohl místo počtu vět zadávat počet slov. Asi by si za počtem slov lépe představil rozsah vygenerovaného textu. Mě osobně se spíše zalíbilo řešení s počtem vět a náhodným generováním slov do těchto vět.

## Nápady, připomínky, chyby

S přibívajícími znalostmi Pythonu mám motivaci tento generátor dále rozvíjet a rozšiřovat, takže byste se v dohledné době mohli dočkat nějaké úpravy/vylepšení.

Pokud je někde chyba, máte nějakou připomínku, chtěli byste do tvorby generátoru nějak přispět, tak se mě nebojte kontaktovat na emailové adrese: *luczka.martin@gmail.com*

**Martin Luczka**
