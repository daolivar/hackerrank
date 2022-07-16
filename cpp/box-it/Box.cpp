class Box {
private:
    int l, b, h;
public:
    Box() {
        l = b = h = 0;
    }

    Box(int l, int b, int h) {
        this->l = l;
        this->b = b;
        this->h = h;
    }

    Box(const Box& b1) {
        this->l = b1.l;
        this->b = b1.b;
        this->h = b1.h;
    }

    int getLength() {
        return l;
    }

    int getBreadth () {
        return b;
    }

    int getHeight() {
        return h;
    }

    long long CalculateVolume() {
        long long vol = l;
        vol *= b;
        vol *= h;
        return vol;
    }

    friend bool operator<( Box const& a, Box const& b) {
        return (a.l < b.l) || (a.b < b.b && a.l == b.l) || (a.h < b.h && b.b == b.b && a.l == b.l);
    }

    friend ostream& operator<<(ostream& os, const Box& bx) {
        os << bx.l << " " << bx.b << " " << bx.h;
        return os;
    }
};
