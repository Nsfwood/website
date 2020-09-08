/* CONTENTFUL */
var contentfulClient = contentful.createClient({
  accessToken: '98b38b929777dffb1f5c2549fd0299e55114a3a9953696cb9d8ce31e9ce5ce42',
  space: '07me4x49e7d7'
})

var PRODUCT_CONTENT_TYPE_ID = 'rating'

var container = document.getElementById('concontent')

contentfulClient.getEntries({
    content_type: PRODUCT_CONTENT_TYPE_ID,
    order: '-fields.dateRated'
  })
  .then(function(entries) {
    container.innerHTML = renderProducts(entries.items)
})

function renderProducts(products) {
	return '<table id="film-table"><tr><th>Name</th><th>Rating</th></tr><tr><td>Check back tomorrow</td><td class="rating-cell">🆕</td></tr>' +
	products.map(renderSingleProduct).join('') +
	'</table>'
}

function renderSingleProduct(product) {
	var fields = product.fields
	return '<tr><td><a href="' +
	fields.link +
        '" title="' +
        fields.reviewText +
	'">' +
	fields.title +
	'</a></td><td class="rating-cell">' +
	fields.rating +
	'</td></tr>'
}