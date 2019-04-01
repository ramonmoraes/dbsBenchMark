# Benchmarking MySQL vs DgraphDB
## Development

Download [this files](https://drive.google.com/open?id=12FPh9wTEirs1BiobYMDecdDCOAf8PUcZ) and unzip it at `/data` folder

```
sudo apt-get install libmysqlclient-dev
pipenv shell --python 3.6 .
```

## Testing

```
pytest
```

updating snapshots
```
pytest --snapshot-update
```

### Obs

The schema cretor uses `set()` which does not mantain the same order, thefore this test usually breaks