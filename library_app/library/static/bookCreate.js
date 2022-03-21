const BookCreate = function(props) {
    const field = {
        
    }
    return <form method="post" enctype="multipart/form-data">
            <div className="row mb-4">
                <div className='col-12'>
                    { field.error? (<div className='bg-danger'> { field.error } </div>) : ''}
                    <label htmlFor='id' ></label>
                    <input id='id' type='text' className="form-control" />
                </div>
            </div>
            <div className="row">
                <div className="col-sm-12 col-md-6 col-lg-4">
                    <div className="row">
                        <div className="col-md-6 col-sm-12 mt-2">
                            <a href="/library" className="btn btn-outline-secondary btn-block">Back</a>
                        </div>
                        <div className="col-md-6 col-sm-12 mt-md-2 mt-4">
                            <input className="btn btn-primary btn-block" type="submit" value="Save" />
                        </div>
                    </div>
                </div>
                <div className="col"></div>
            </div>
        </form>;
}

