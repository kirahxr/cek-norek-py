from datetime import datetime
import json

with open('data.json') as f:
    data_bank = json.load(f)


def remove_end_spaces(string):
    return "".join(string.rstrip())


def format_data(params, norek, kode_bank):
    response = {}

    if params['status'] == '0000':
        response.update({
            'err': False,
            'message': 'success',
            'data': {
                'kode_bank': kode_bank,
                'nomor_rekening': norek,
                'nama_bank': filtered(kode_bank),
                'nama_pemilik': remove_end_spaces(params['data']['name'])
            },
            'date': datetime.now()
        })

    if params['status'] != '0000':
        response.update({
            'err': True,
            'message': 'failed',
            'date': datetime.now()
        })

    return response


def filter_set(daftar_kodebank, search_string):
    def iterator_func(x):
        for v in x.values():
            if search_string in v:
                return True
        return False

    return filter(iterator_func, daftar_kodebank)


def filtered(kode_bank):
    filtered_records = filter_set(data_bank, kode_bank)
    result = list(filtered_records)

    return result[0]['label']
