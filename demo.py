import json
from pathlib import Path
from geometry import transport
from identity import pairwise

if __name__=='__main__':
    data=json.loads((Path(__file__).parent/'fixtures/cases.json').read_text())
    print(json.dumps({'transport':transport(**data['ordinary_transport']),
                      'identity':pairwise(data['ordinary_affinities'])},indent=2))
