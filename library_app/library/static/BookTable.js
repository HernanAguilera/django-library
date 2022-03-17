const BookTable = function(props) {
    return <div className="row"> {props.books.map((book, index) => {
        return <div className="col-sm col-md-4 col-lg-3 mb-2" key={index}>
            <div className="card">
                <a href={ `/library/${ book.pk }` }>
                    <img src={ `/media/${book.fields.cover}` } className="card-img-top" />
                </a>
                <div className="card-body">
                    <h5 className="card-title">
                        <a href={ `/library/${book.pk}` }>
                            { book['fields']['name'] }
                        </a>
                    </h5>
                    <p className="card-text"> { book.fields.summary } </p>
                    <a href={ `/library/${book.pk}/edit` } className="card-link">Edit</a>
                </div>
            </div>
        </div>;
    })} </div>;
}