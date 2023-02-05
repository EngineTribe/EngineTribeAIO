# Engine Tribe AIO

This is the all-in-one package for Engine Tribe, can be used for hosting services like Vyxterhost.

### Usage

```bash
git submodule update --init
python3 -m venv venv
source venv/bin/activate
for module in "enginetribe", "enginebot_discord"; do
  pushd ${module}
  git pull
  pip3 install -r requirements.txt
  popd
done
python3 -m main
```