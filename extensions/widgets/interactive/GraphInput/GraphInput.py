# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Zhan Xiong Chin'

from core.domain import widget_domain
from extensions.value_generators.models import generators

class GraphInput(widget_domain.BaseWidget):
    """Interactive widget for graphs."""
       
    # The human-readable name of the widget.
    name = 'Graph Input'

    # The category the widget falls under in the widget repository.
    category = 'Custom'
    
    # A descrption of the widget.
    description = 'A widget where users create and manipulate graphs.'
    
    # Customization parameters and their descriptions, schemas and default
    # values.
    _customization_arg_specs = [{
        'name': 'graph',
        'description': 'The initial graph.',
        'schema': {
            'type': 'custom',
            'obj_type': 'Graph',
        },
        'default_value': {
            'vertices': [{
                'x': 150.0,
                'y': 50.0,
                'label': '',
            }, {
                'x': 200.0,
                'y': 50.0,
                'label': '',
            }, {
                'x': 150.0,
                'y': 100.0,
                'label': '',
            }],
            'edges': [{
                'src': 0,
                'dst': 1,
                'weight': 1,
            }, {
                'src': 1,
                'dst': 2,
                'weight': 1,
            }],
            'isLabeled': False,
            'isDirected': False,
            'isWeighted': False,
        }
    }, {
        'name': 'canAddVertex',
        'description': 'Add vertices',
        'schema': {
            'type': 'bool',
        },
        'default_value': False 
    }, {
        'name': 'canDeleteVertex',
        'description': 'Delete vertices',
        'schema': {
            'type': 'bool',
        },
        'default_value': False
    }, {
        'name': 'canMoveVertex',
        'description': 'Move vertices',
        'schema': {
            'type': 'bool',
        },
        'default_value': True
    }, {
        'name': 'canEditVertexLabel',
        'description': 'Edit vertex labels',
        'schema': {
            'type': 'bool',
        },
        'default_value': False
    }, {
        'name': 'canAddEdge',
        'description': 'Add edges',
        'schema': {
            'type': 'bool',
        },
        'default_value': True
    }, {
        'name': 'canDeleteEdge',
        'description': 'Delete edges',
        'schema': {
            'type': 'bool',
        },
        'default_value': True
    }, {
        'name': 'canEditEdgeWeight',
        'description': 'Edit edge weights',
        'schema': {
            'type': 'bool',
        },
        'default_value': False
    }]

    # Actions that the reader can perform on this widget which trigger a
    # feedback interaction, and the associated input types. Interactive widgets
    # must have at least one of these. This attirbute name MUST be prefixed by
    # '_'.
    _handlers = [{
        'name': 'submit', 'obj_type': 'Graph'   
    }]

    # Additional JS library dependencies that should be loaded in pages
    # containing this widget. These should correspond to names of files in
    # feconf.DEPENDENCIES_TEMPLATES_DIR.
    _dependency_ids = []
