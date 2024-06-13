# soar-path-maker
Single python script to generate SOAR data path according to endpoint API response

# Usage
Before run python Script copy paste your API endpoint response into **response_scheme.json** file, Python script is based on the content of this file.

Next thing is to check whether API returns content for signle data i.e 
 ```json
 {
    "group_val": "nongroup",
    "asset_type_string": "CodeRepository",
    "alert_labels": [
        "shiftleft:iac",
        "source:shiftleft"
    ],
    "configuration": {},
    "is_compliance": false,
     "cluster_unique_id": "CodeRepository_94c4b3a3-fe76-4537-816d-62b36634dd09_c46cb523-9c82-5929-eca0-aeff08ca7854",
    "cluster_name": "tomerb-orca/terragoat-2",
    "subject_type": "CodeRepository_94c4b3a3-fe76-4537-816d-62b36634dd09_c46cb523-9c82-5929-eca0-aeff08ca7854",
    "group_name": "tomerb-orca/terragoat-2",
    "level": 0
 }
 ```

 Or more data i.e

 ```json
 {
    "data": [
        {
            "type": "_generic",
            "is_rule": "bool",
            "rule_query": "string",
            "is_compliance": "bool",
            "user_defined": "bool",
            "rule_id": "string",
            "subject_type": "string",
            "asset_stopped": "bool",
            "asset_role_names": [
                "string"
            ],
            "asset_ingress_ports": [
                "string"
            ],
            "asset_availability_zones": [
                "string"
            ]
        }
    ]
 }
```
User just need to focus on parameter **DATA_KEY**, wheter want to focus on whole file content or content nested under some key in .json file
