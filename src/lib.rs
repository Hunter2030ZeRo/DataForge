use pyo3::prelude::*;

#[pymodule]
mod dataforge {
    use pyo3::prelude::*;

    #[pyclass]
    struct Dataset {}

    #[pyfunction]
    fn map(dataset: &Dataset) -> Dataset {}
}
