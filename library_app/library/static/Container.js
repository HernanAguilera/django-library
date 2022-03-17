class httpClient {
    get(url, filters) {
        const config = {
            headers: {
              'Content-Type': 'application/json'
            },
        }
        return fetch(url).then(res => res.json())
    }
}

const http = new httpClient();

class ContainerComponent extends React.Component {

    constructor(props) {
        super(props);
        this.state = { books: this.props.books };
    }

    handleChange(e) {
        console.log('evento', e.target.value);
        let url = e.target.value === null? '/library/books-json' : `/library/books-json?category=${e.target.value}`
        http.get(url).then(res => {
            console.log('response', JSON.parse(res.books))
            this.setState({ books: JSON.parse(res.books)})
        })
    }

    render() {
        return (
            <div className="col-12">
                <FiltersTable categories={this.props.categories} handleChange={this.handleChange.bind(this)} />
                <BookTable books={this.state.books} />
            </div>
        );
    }
}