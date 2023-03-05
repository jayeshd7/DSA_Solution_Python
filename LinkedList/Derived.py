from Arrays.Base import Base

assert hasattr(Base, 'foo'),"you broke it you fool:"
class Derived(Base):
    def bar(self):
        return self.foo(self)

if __name__ == '__main__':
    d = Derived
    print(d.bar(d))
