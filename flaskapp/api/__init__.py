from flask import Blueprint, jsonify
import json, os

api = Blueprint('api', __name__, 
                    static_folder=None, 
                    static_url_path=None,
                    template_folder=None)

api.spells = None
api.monsters = None

@api.route('/spells')
def spellsrt():
    if not api.spells:
        with open('data/5e-SRD-Spells.json') as spellsfile:
            api.spells = json.load(spellsfile)
    return jsonify(api.spells)

@api.route('/monsters')
def monstersrt():
    if not api.monsters:
        with open('data/5e-SRD-Monsters.json') as monstersfile:
            api.monsters = json.load(monstersfile)
    return jsonify(api.monsters)


