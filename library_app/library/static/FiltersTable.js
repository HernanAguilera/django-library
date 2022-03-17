const FiltersTable = function(props) {
    return (
        <div className="row">
            <div className="col">
                <div className="form-group">
                    <label htmlFor="searchSelect">Filter by category:</label>
                    <select id="searchSelect" className="form-control" onChange={props.handleChange}>
                        <option value="">-----------</option>
                        { props.categories.map((category, index) => {
                            return <option value={category.pk} key={index} >
                                        {category.fields.description}
                                    </option>
                        }) }
                    </select>
                    <hr />
                </div>
            </div>
        </div>

    );
}