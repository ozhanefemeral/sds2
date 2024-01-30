gsap.registerPlugin(ScrollToPlugin)

const nav = $('nav');
var currGenerator; //Needed for form.js

function fillContent(generator_name){

    currGenerator = generator_name;
    
    $("#SecOutput").hide();    
    $("#SecTests").hide();
    $("form button").removeClass("clickedOnce")

    gsap.to(window, { duration: 1, scrollTo: $("#SecInfo").position().top ,ease: "power2" });

    nav.find('ul>li').removeClass('selected')

    const secInfo = $('#SecInfo')
    const form = $("#myform");

    const lorem_ipsum_txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eleifend ornare ultrices. Vestibulum mauris mauris, interdum vel vulputate in, dictum quis risus. Suspendisse vehicula facilisis dolor id porta. Nullam convallis augue tristique egestas consequat. Proin a pretium nunc. Ut aliquam velit at sodales viverra. Donec dignissim molestie nunc sed sollicitudin. Curabitur pretium quis purus suscipit ultricies. Phasellus lacinia est lorem, et hendrerit metus sollicitudin sit amet. Aliquam tempus bibendum aliquet."

    switch(generator_name){

        case "Xoshiro":
            nav.find('ul>li').eq(0).addClass('selected');

            var infoContent = `
                <h1>Generator Xoshiro256</h1>
                <p>Generator Xoshiro256** jest generatorem liczb pseudolosowych, wywodzi się on z rodziny generatorów Xoshiro, której nazwa jest skrótem od „xor-shift-rotate” co odnosi się do głównych operacji wykorzystywanych w algorytmie. </p>
                <p>Xoshiro256** używa liniowego silnika Xoshiro256 oraz szyfratora „**” , który wykonuje operację mnożenia, obrotu oraz ponownego mnożenia.</p>
                <p> Parametrem wejściowym algorytmu generatora jest ziarno w formie 64-bitowej liczby bez znaku, a dodatkowo udostępniono możliwość ograniczenia długości wygenerowanego ciągu przy pomocy parametru bit size.`;
            secInfo.html(infoContent)

            var formContent = `
                <div>
                    <label>seed</label>
                    <input type="text" name="seed" size="10" placeholder="30"/>
                </div>
                <div>
                    <label>bit size</label>
                    <input type="text" name="bitsize" size="10" placeholder="50 "/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;
        
        case "MSWS":
            nav.find('ul>li').eq(1).addClass('selected');

            var infoContent = `
                <h1>Generator Middle Square Weyl Sequence</h1>
                <p>Generator Middle Square Weyl Sequence jest rozwinięciem generatora Middle Square. Został opracowany przez Bernarda Widynskiego. Główna zmiana polega na wpleceniu sekwencji Weyla w algorytm, aby wyeliminować główny problem oryginalej wersji, czyli wpadanie w pętle.</p>
                <p>Na wejściu zaimplementowany generator przyjmuję tylko ziarno w postaci liczby 64-bitowej oraz długość ciągu pseudolosowego, który chcemy otrzymać wyrażoną w bitach</p>`;
            secInfo.html(infoContent)

            var formContent = `
                <div>
                    <label>seed</label>
                    <input type="text" name="seed" size="10" placeholder="1234"/>
                </div>
                <div>
                    <label>bit size</label>
                    <input type="text" name="bitsize" size="10" placeholder="30"/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;

        case "MM":
            nav.find('ul>li').eq(2).addClass('selected');
            
            var infoContent = `
                <h1>Generator McLaren-Marsaglia</h1>
                <p>Generator tasuje ciąg/wyjście generatora X na podstawie wartości generatora Y.<br>Generator początkowo inicjalizuje tablice przejściową V k-wartościami generatora X, następnie generator wybiera która wartość ma opuścić tablice i pojawić się na wyjściu na podstawie kolejnej wartości generatora Y. Kiedy wartość opuszcza tablice V zastępuje ją w tablicy kolejna wartość generatora X.</p>
                <p>Aby skorzystać z wersji gdzie podajemy własny ciąg X i Y należy podać ciąg liczb niebitowych wygenerowanych przez generator X w polu X, a przez generator Y w polu Y, k gdzie k - wielkość tablicy inicjującej V i k <= size(X), n gdzie n - długość ciągu jaki chcemy otrzymać.<br>	W przypadku gdy chcemy podać na wejście generatory LCG pola X i Y należy pozostawić puste, wypełnić pola k, n, oraz pola aX, cX, mX, seedX i analogiczne dla generatora Y wypełnić parametrami generatorów LCG gdzie LCG generuje liczby w sposób następujący: <br> - X(0) = seedX<br> - X(n+1)=(aX*X(n)+bX)mod mX</p>`;
            secInfo.html(infoContent)

            var formContent = `
            
                <div>
                    <label>X</label>
                    <input type="text" name="X" size="30" placeholder="0 1 2 3 ..."/>
                </div>
                <div>
                    <label>Y</label>
                    <input type="text" name="Y" size="30" placeholder="0 1 2 3 ..."/>
                </div>

                <div>
                    <label>k</label>
                    <input type="text" name="k" size="10" placeholder="64"/>
                </div>
                <div>
                    <label>n</label>
                    <input type="text" name="n" size="10" placeholder="100"/>
                </div>

                <div>
                    <label>aX</label>
                    <input type="text" name="aX" size="10" placeholder="3141592653"/>
                </div>
                <div>
                    <label>cX</label>
                    <input type="text" name="cX" size="10" placeholder="2718281829"/>
                </div>
                <div>
                    <label>mX</label>
                    <input type="text" name="mX" size="10" placeholder="35"/>
                </div>
                <div>                
                    <label>seedX</label>
                    <input type="text" name="seedX" size="10" placeholder="5772156649"/>
                </div>

                <div>
                    <label>aY</label>
                    <input type="text" name="aY" size="10" placeholder="2718281829"/>
                </div>
                <div>
                    <label>cY</label>
                    <input type="text" name="cY" size="10" placeholder="3141592653"/>
                </div>
                <div>
                    <label>mY</label>
                    <input type="text" name="mY" size="10" placeholder="35"/>
                </div>
                <div>                
                    <label>seedY</label>
                    <input type="text" name="seedY" size="10" placeholder="1781072418"/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;

        case "BD":
            nav.find('ul>li').eq(3).addClass('selected');
            
            var infoContent = `
                <h1>Generator Bays-Durham</h1>
                <p>Generator tasuje ciąg/wyjście generatora X.<br>Generator początkowo inicjalizuje tablice przejściową V k-wartościami generatora X, oraz ustawia zmienną Y na k+1-wartość generatora X, następnie generator ustawia zmienną x jako kolejną wartość generatora X, na podstawie Y obliczana jest wartość j, następnie algorytm ustawia Y = V[j], na wyjście podaje Y i ustawia V[j] = x.</p>
                <p>Aby skorzystać z wersji gdzie podajemy własny ciąg X należy podać ciąg liczb niebitowych wygenerowanych przez generator X w polu X, k gdzie k - wielkość tablicy inicjującej V i k <= size(X), n gdzie n - długość ciągu jaki chcemy otrzymać.<br>	W przypadku gdy chcemy podać na wejście generator LCG pole X należy pozostawić puste, wypełnić pola k, n, oraz pola aX, cX, mX, seedX wypełnić parametrami generatora LCG gdzie LCG generuje liczby w sposób następujący: <br> - X(0) = seedX<br> - X(n+1)=(aX*X(n)+bX)mod mX</p>`;
            secInfo.html(infoContent)

            var formContent = `

                <div>
                    <label>X</label>
                    <input type="text" name="X" size="30" placeholder="0 1 2 3 ..."/>
                </div>

                <div>
                    <label>k</label>
                    <input type="text" name="k" size="10" placeholder="64"/>
                </div>
                <div>
                    <label>n</label>
                    <input type="text" name="n" size="10" placeholder="100"/>
                </div>

                <div>
                    <label>aX</label>
                    <input type="text" name="aX" size="10" placeholder="3141592653"/>
                </div>
                <div>
                    <label>cX</label>
                    <input type="text" name="cX" size="10" placeholder="2718281829"/>
                </div>
                <div>
                    <label>mX</label>
                    <input type="text" name="mX" size="10" placeholder="35"/>
                </div>
                <div>                
                    <label>seedX</label>
                    <input type="text" name="seedX" size="10" placeholder="5772156649"/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;
        
        case "WELL":
            nav.find('ul>li').eq(4).addClass('selected');

            var infoContent = `
                <h1>Generator WELL512a</h1>
                <p> Twórcami algorytmu generatora są: <i>François Panneton, Pierre L’Ecuyer</i> oraz <i>Makoto Matsumoto</i>.<br>
                    W celu uzyskania pseudolosowości autorzy w algorytmie zastosowali mechanizmy przesunięć bitowych
                    zarówno w lewo, jak i w prawo, operacje bitowe AND oraz XOR czy też maski bitowe.</p>

                <p> Ważnymi cechami generatora są zarówno jego 32-bitowa architektura, idealnie nadająca się
                    do zastosowań w systemach komputerowych, jak i długi okres powtarzalności ciągu, po którym generowany
                    ciąg zaczyna się odtwarzać. Cechy te sprawiają, że idealnie nadaje się do różnych symulacji komputerowych
                    wymagających długich pseudolosowych ciągów danych.</p>

                <p> Parametr <b>seed</b> określa początkowy wektor stanu, składający się z 16 oddzielonych spacją bądź przecinkami liczb
                    całkowitych z zakresu <b>[0, 4294967295]</b>.<br>
                    Parametr <b>size</b> określa ilość wartości do wygenerowania i jest liczbą całkowitą nieujemną. W celu wykonania testów statystycznych parametr ten powinien
                    być większy niż <b>625</b> </p>
                `;
            secInfo.html(infoContent)

            var formContent = `
                <div>
                    <label>seed</label>
                    <input type="text" name="seed" size="30" placeholder="0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15"/>
                </div>
                <div>
                    <label>size</label>
                    <input type="text" name="size" size="10" placeholder="100"/>
                </div>
            `;
            form.find("#formContent").html(formContent)

            break;
    }

}

nav.find('ul>li').on('click', function () {
    fillContent($(this).text());
});

fillContent(nav.find('ul>li').eq(0).text())