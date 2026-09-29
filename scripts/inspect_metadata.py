import pickle, os, sys
p = os.path.abspath(os.path.join('models','vector_index','metadata.pkl'))
print('path', p)
if not os.path.exists(p):
    print('metadata file not found')
    sys.exit(1)
with open(p,'rb') as f:
    data = pickle.load(f)
print('type', type(data))
print('len', len(data) if hasattr(data,'__len__') else 'n/a')
for i, item in enumerate(data[:10]):
    print(i, type(item), repr(item))
