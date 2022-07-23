/*Write the class AddElements here*/
template <class T> class AddElements {
    public:
        T element;
        AddElements(T arg) {
            element = arg;
        }
        T add(T arg) { 
            return element + arg;
        }
    private:
        
};

template <> class AddElements <string> {
    public:
        string element;
        AddElements(string arg) {
            element = arg;
        }
        string concatenate(string arg) {
            return element+arg;
        }
    private:
        
};
