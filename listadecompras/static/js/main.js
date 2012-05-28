function atualizar() {
    var storage = sessionStorage;

    $('li.produto').each(function(index) {
        if (storage.getItem(this.id) !== null) {
            $(this).attr("data-icon", "check");
        } else {
            $(this).attr("data-icon", "plus");
        }
    });
}

function totalItensNaLista() {
    $('#totalItensNaLista').html(sessionStorage.length);
}

function _trocaIcone(elemento, atual, novo) {
    $('#' + elemento.id).data('icon', novo);
    $('#' + elemento.id + ' .ui-icon').addClass('ui-icon-' + novo).removeClass('ui-icon-' + atual);
}

function adicionar(elemento) {
    var storage = sessionStorage,
        produto = $('#link'+elemento.id).text(),
        value = storage.getItem(elemento.id);
        
    if (value !== null) {
        storage.removeItem(elemento.id);
        _trocaIcone(elemento, 'check', 'plus');
    }
    else {
        storage.setItem(elemento.id, produto);
        _trocaIcone(elemento, 'plus', 'check');
    }
    //totalItensNaLista();
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
            error: function(retorno) {
               lista.append('<li>Nenhum produto na se&ccedil;&atilde;o</li>');
            }
        });
    }
}

function resumoDaLista() {
    var form = $('#listaDeProdutos'),
        storage = sessionStorage,
        listaDeIds = [];

    for (i = 0; i < storage.length; i++) {
        listaDeIds.push(storage.key(i));
    }
    form.append('<input type="hidden" name="ids" value="' + listaDeIds.toString() + '">');
    form.submit();
}

function limparStorage() {
    sessionStorage.clear();
}

function teclaSoPodeSerNumero(evt) {
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    return ! (charCode > 31 && (charCode < 48 || charCode > 57));
}

function finalizarLista() {
    var data = $('input[type=text].quantidade').serializeArray();

    if (data.length > 0) {

        $.ajax({
            url: '/lista/finalizar/',
            type: 'POST',
            data: data,
            success: function(retorno) {
                limparStorage();
                window.location.href = retorno.url;
            },
            error: function(retorno) {
               alert('Houve um erro ao salvar a lista. Crie outra!');
            }
        });
    }
}

function riscar(elemento) {
    $('#'+elemento.id).toggleClass('riscado');
}

function finalizar() {
    var form = $('#listaDeProdutos'),
        storage = sessionStorage,
        listaDeIds = [];

    for (i = 0; i < storage.length; i++) {
        listaDeIds.push(storage.key(i));
    }
    form.append('<input type="hidden" name="ids" value="' + listaDeIds.toString() + '">');
    form.submit();
}