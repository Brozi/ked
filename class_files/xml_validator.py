from xmlschema import XMLSchema


def validate(xsd_file, xml_file):
    s = XMLSchema(xsd_file)
    print(s.is_valid(xml_file))
    for e in s.iter_errors(xml_file):
        print(e)


validator = 'jakis_plik_definition.xsd'
to_validate = 'jakis_plik.xml'
validate(validator, to_validate)
