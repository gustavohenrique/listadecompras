function atualizar() {
    var storage = sessionStorage;

    $('a.item').each(function(index) {
        if (storage.getItem(this.id) != null) {
            this.childNodes[0].setAttribute("class", "icon-ok");
        } else {
            this.childNodes[0].setAttribute("class", "icon-plus");
        }

    });
}

function totalItensNaLista() {
    $('#totalItensNaLista').html(sessionStorage.length);
}

function adicionar(elemento) {
    var storage = sessionStorage,
        produto = elemento.parentNode.textContent,
        value = storage.getItem(elemento.id);
        //elemento.parent().text()

    if (value != null) {
        storage.removeItem(elemento.id);
        elemento.childNodes[0].setAttribute("class", "icon-plus");
    }
    else {
        storage.setItem(elemento.id, produto);
        elemento.childNodes[0].setAttribute("class", "icon-ok");
    }
    totalItensNaLista();
}

function exibirProdutos(elemento) {
    var secao_id = $('#' + elemento.id + ' option:selected').val(),
        lista = $('#produtos');

    if (secao_id > 0) {
        lista.empty();
        $.ajax({
            url: '/lista/produtos/' + secao_id + '/',
            success: function(retorno) {
                $.each(retorno, function(i, item) {
                    lista.append('<li><a href="#" id="' + item.pk + '" class="item" onclick="adicionar(this)"><i class="icon-plus"></i>&nbsp;</a>' + item.fields['nome'] + '</li>');
                });
                atualizar();
            },
            error: function(data) {
               lista.append('<li>Nenhum produto na se&ccedil;&atilde;o</li>');
            }
        });
    }
}

function salvarLista() {
    var form = $('#listaDeProdutos'),
        storage = sessionStorage,
        listaDeIds = new Array();

    for (i = 0; i < storage.length; i++) {
        listaDeIds.push(storage.key(i));
    }
    form.append('<input type="hidden" name="ids" value="' + listaDeIds.toString() + '">');
    form.submit();
}

function limparStorage() {
    sessionStorage.clear();
    history.go(0);
}

function teclaSoPodeSerNumero(evt) {
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    return ! (charCode > 31 && (charCode < 48 || charCode > 57));
}