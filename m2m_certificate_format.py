#! /usr/bin/env python3

"""Format for M2M certificates as defined in
Signature Record Type Definition
Technical Specification
Version 2.0
2014-11-26
[SIGNATURE]
NFC Forum (tm)

[SEC1]:
STANDARDS FOR EFFICIENT CRYPTOGRAPHY
SEC 1: Elliptic Curve Cryptography
September 20, 2000
Version 1.0
http://www.secg.org/SEC1-Ver-1.0.pdf"""

# Originally:
# Auto-generated by asn1ate v.0.5.1.dev from M2M-Certificate-Definition.asn1
# (last modified on 2016-07-08 14:43:12.164589)

from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful
from pyasn1.codec.der import encoder as der_encoder
import binascii
import enum
import base64
import subprocess


class ChoiceCouldMatchMixin(object):  # is actually univ.Choice but that of course messed with Method Resolution Order
    def could_match(self, other, debug=False):
        """Check whether other could be a match to self.
        The other lost the field names after decoding, so we simply check all the field self might have and return the field names that matches.
        If there is no matching value, return None"""
        choices = [component_type.getName() for component_type in self.componentType]
        choice_value_map = {choice: self[choice] for choice in choices}
        choice_values = [(choice, val) for choice, val in choice_value_map.items() if val]
        if choice_values:
            choice, value = choice_values[0]
            if value == other:
                if debug: print("a[{choice}] == b == {value}".format(choice=choice, value=value))
                return choice
            else:
                return None

class SequenceOfCouldMatchMixin(object):  # is actually univ.Sequence but that of course messed with Method Resolution Order
    def could_match(self, other, debug=False):
        """Check that, in order, all the elements could match the other sequence"""
        for a, b in zip(self, other):
            if hasattr(a, 'could_match'): # Only custom elements that use the mixins above have the attribute.
                if not a.could_match(b, debug=debug):
                    if debug: print("{a} could not match {b}: {a} !~= {b}".format(a=a, b=b))
                    return False
            else:  # If they don't have the attribute, then check for normal equality
                if not a == b:
                    import ipdb; ipdb.set_trace()
                    if debug: print("{a} does not match {b}: {a} != {b}".format(a=a, b=b))
                    return False
        return True

class SequenceCouldmatchMixin(object):  # is actually univ.Sequence but that of course messed with Method Resolution Order
    def could_match(self, other, debug=False):
        """Check that, in order, all the elements could match the other sequence"""
        # import ipdb; ipdb.set_trace()
        elements = [component_type.getName() for component_type in self.componentType]
        elements_with_value = [element for element in elements if self[element] != None]

        #for a, b in zip(self, other):
        for index, element in enumerate(elements_with_value):
            a, b = self[element], other[index]
            if hasattr(a, 'could_match'): # Only custom elements that use the mixins above have the attribute.
                if not a.could_match(b, debug=debug):
                    if debug: print("{a} could not match {b}: {a} !~= {b}".format(a=a, b=b))
                    return False
            else:  # If they don't have the attribute, then check for normal equality
                if not a == b:
                    import ipdb; ipdb.set_trace()
                    if debug: print("{a} does not match {b}: {a} != {b}".format(a=a, b=b))
                    return False
        return True


class AttributeValue(univ.Choice, ChoiceCouldMatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('country',
                            char.PrintableString().subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2))),
        namedtype.NamedType('organization',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))),
        namedtype.NamedType('organizationalUnit',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))),
        namedtype.NamedType('distinguishedNameQualifier',
                            char.PrintableString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))),
        namedtype.NamedType('stateOrProvince',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 4))),
        namedtype.NamedType('locality',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))),
        namedtype.NamedType('commonName',
                            char.UTF8String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))),
        namedtype.NamedType('serialNumber',
                            char.PrintableString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))),
        namedtype.NamedType('domainComponent',
                            char.IA5String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))),
        namedtype.NamedType('registeredId', univ.ObjectIdentifier()),
        namedtype.NamedType('octetsName',
                            univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8)))
    )

    def __init__(self, country=None, 
        organization=None, organizationalUnit=None, 
        distinguishedNameQualifier=None, 
        stateOrProvince=None, locality=None, 
        commonName=None, serialNumber=None, 
        domainComponent=None, 
        registeredId=None, octetsName=None):
        super(AttributeValue, self).__init__()

        values = [country, organization, organizationalUnit, distinguishedNameQualifier, stateOrProvince, locality, commonName, serialNumber, domainComponent, registeredId, octetsName]
        if len([value for value in values if value != None]) > 1:
            raise ValueError("AttributeValue is a Choice, supply only 1 argument")

        if country:
            self['country'] = char.PrintableString(country)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(2, 2))
        if organization:
            self['organization'] = char.UTF8String(organization)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))
        if organizationalUnit:
            self['organizationalUnit'] = char.UTF8String(organizationalUnit)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))
        if distinguishedNameQualifier:
            self['distinguishedNameQualifier'] = char.PrintableString(distinguishedNameQualifier)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))
        if stateOrProvince:
            self['stateOrProvince'] = char.UTF8String(stateOrProvince)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 4))
        if locality:
            self['locality'] = char.UTF8String(locality)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))
        if commonName:
            self['commonName'] = char.UTF8String(commonName)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))
        if serialNumber:
            self['serialNumber'] = char.PrintableString(serialNumber)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))
        if domainComponent:
            self['domainComponent'] = char.IA5String(domainComponent)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 32))
        if registeredId:
            self['registeredId'] = univ.ObjectIdentifier(registeredId)
        if octetsName:
            self['octetsName'] = univ.OctetString(octetsName)#.subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 8))

    @staticmethod
    def new(*args, **kwargs):
        return AttributeValue(*args, **kwargs)


class Name(univ.SequenceOf, SequenceOfCouldMatchMixin):
    componentType = AttributeValue()
    subtypeSpec=constraint.ValueSizeConstraint(1, 4)

    @staticmethod
    def new(*items):
        if len(items) < Name.subtypeSpec.start:
            raise ValueError("Too few items: need at least {min}".format(min=Name.subtypeSpec.start))
        if len(items) > Name.subtypeSpec.stop:
            raise ValueError("Too many items: can accept at most {max}".format(max=Name.subtypeSpec.stop))

        name = Name()
        for i, item in enumerate(items):
            name[i] = item

        return name


class GeneralName(univ.Choice, ChoiceCouldMatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('rfc822Name',
                            char.IA5String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128))),
        namedtype.NamedType('dNSName',
                            char.IA5String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128))),
        namedtype.NamedType('directoryName', Name()),
        namedtype.NamedType('uniformResourceIdentifier',
                            char.IA5String().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128))),
        namedtype.NamedType('iPAddress',
                            univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 16))),
        namedtype.NamedType('registeredID', univ.ObjectIdentifier())
    )

    @staticmethod
    def new(rfc822Name=None, dNSName=None, directoryName=None, uniformResourceIdentifier=None, iPAddress=None, registeredID=None):
        general_name = GeneralName()

        if rfc822Name:
            general_name['rfc822Name'] = char.IA5String(rfc822Name).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128))
        if dNSName:
            general_name['dNSName'] = char.IA5String(dNSName).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128))
        if directoryName:
            general_name['directoryName'] = directoryName # Name(directoryName)
        if uniformResourceIdentifier:
            general_name['uniformResourceIdentifier'] = char.IA5String(uniformResourceIdentifier).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 128))
        if iPAddress:
            general_name['iPAddress'] = univ.OctetString(iPAddress).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 16))
        if registeredID:
            general_name['registeredID'] = univ.ObjectIdentifier(registeredID)

        return general_name


class AuthKeyId(univ.Sequence, SequenceCouldmatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.OptionalNamedType('keyIdentifier', univ.OctetString()),
        namedtype.OptionalNamedType('authCertIssuer', GeneralName()),
        namedtype.OptionalNamedType('authCertSerialNum', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 20)))
    )

    @staticmethod
    def new(keyIdentifier=None, authCertIssuer=None, authCertSerialNum=None):
        authKeyId = AuthKeyId()
        if keyIdentifier:
            octet_string_subtype = univ.OctetString(value=keyIdentifier)
            # der_encoder.encode(octet_string_subtype)
            authKeyId['keyIdentifier'] = octet_string_subtype
        if authCertIssuer:
            cert_issuer_subtype = authCertIssuer#
            der_encoder.encode(cert_issuer_subtype)
            authKeyId['authCertIssuer'] = cert_issuer_subtype
        if authCertSerialNum:
            octet_string_subtype2 = univ.OctetString(value=authCertSerialNum).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 20))
            # der_encoder.encode(octet_string_subtype2)
            authKeyId['authCertSerialNum'] = octet_string_subtype2

        return authKeyId


class Extension(univ.Sequence, SequenceCouldmatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('extnID', univ.ObjectIdentifier()),
        namedtype.DefaultedNamedType('criticality', univ.Boolean().subtype(value=0)),
        namedtype.NamedType('extnValue', univ.OctetString())
    )

    @staticmethod
    def new(extnID, criticality, extnValue):
        extension = Extension()
        extension['extnID'] = univ.ObjectIdentifier(extnID)
        extension['criticality'] = univ.Boolean(criticality).subtype(value=0)
        extension['extnValue'] = univ.OctetString(extnValue)

        return extension


class X509Extensions(univ.SequenceOf):
    componentType = Extension()

    @staticmethod
    def new(*items):
        x509exts = X509Extensions()
        for i, item in enumerate(items):
            x509exts[i] = item

        return x509exts


class TBSCertificate(univ.Sequence, SequenceCouldmatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.DefaultedNamedType('version', univ.Integer()),
        namedtype.NamedType('serialNumber', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 20))),
        namedtype.OptionalNamedType('cAAlgorithm', univ.ObjectIdentifier()),
        namedtype.OptionalNamedType('cAAlgParams', univ.OctetString()),
        namedtype.OptionalNamedType('issuer', Name()),
        namedtype.OptionalNamedType('validFrom', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 5))),
        namedtype.OptionalNamedType('validDuration', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 4))),
        namedtype.NamedType('subject', Name()),
        namedtype.OptionalNamedType('pKAlgorithm', univ.ObjectIdentifier()),
        namedtype.OptionalNamedType('pKAlgParams', univ.OctetString()),
        namedtype.OptionalNamedType('pubKey', univ.OctetString()),
        namedtype.OptionalNamedType('authKeyId', AuthKeyId()),
        namedtype.OptionalNamedType('subjKeyId', univ.OctetString()),
        namedtype.OptionalNamedType('keyUsage', univ.OctetString().subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1))),
        namedtype.OptionalNamedType('basicConstraints', univ.Integer().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))),
        namedtype.OptionalNamedType('certificatePolicy', univ.ObjectIdentifier()),
        namedtype.OptionalNamedType('subjectAltName', GeneralName()),
        namedtype.OptionalNamedType('issuerAltName', GeneralName()),
        namedtype.OptionalNamedType('extendedKeyUsage', univ.ObjectIdentifier()),
        namedtype.OptionalNamedType('authInfoAccessOCSP', char.IA5String()),
        namedtype.OptionalNamedType('cRLDistribPointURI', char.IA5String()),
        namedtype.OptionalNamedType('x509extensions', X509Extensions())
    )

    @staticmethod
    def new(version, serialNumber, 
            subject, 
            cAAlgorithm=None, cAAlgParams=None, 
            issuer=None, 
            validFrom=None, validDuration=None, 
            pKAlgorithm=None, pKAlgParams=None, 
            pubKey=None, authKeyId=None, subjKeyId=None, keyUsage=None, basicConstraints=None, certificatePolicy=None, 
            subjectAltName=None, issuerAltName=None, 
            extendedKeyUsage=None, authInfoAccessOCSP=None, cRLDistribPointURI=None, 
            x509extensions=None):
        tbs = TBSCertificate()

        tbs['version'] = univ.Integer(value=version, namedValues=namedval.NamedValues(('v1', 0))).subtype(value='v1')
        tbs['serialNumber'] = univ.OctetString(serialNumber).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 20))
        if cAAlgorithm: tbs['cAAlgorithm'] = univ.ObjectIdentifier(cAAlgorithm)
        if cAAlgParams: tbs['cAAlgParams'] = univ.OctetString(cAAlgParams)
        if issuer: tbs['issuer'] = issuer
        if validFrom: tbs['validFrom'] = univ.OctetString(validFrom).subtype(subtypeSpec=constraint.ValueSizeConstraint(4, 5))
        if validDuration: tbs['validDuration'] = univ.OctetString(validDuration).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 4))
        tbs['subject'] = subject
        if pKAlgorithm: tbs['pKAlgorithm'] = univ.ObjectIdentifier(pKAlgorithm)
        if pKAlgParams: tbs['pKAlgParams'] = univ.OctetString(pKAlgParams)
        if pubKey: tbs['pubKey'] = univ.OctetString(pubKey)
        if authKeyId: tbs['authKeyId'] = authKeyId
        if subjKeyId: tbs['subjKeyId'] = univ.OctetString(subjKeyId)
        if keyUsage: tbs['keyUsage'] = univ.OctetString(keyUsage).subtype(subtypeSpec=constraint.ValueSizeConstraint(1, 1))
        if basicConstraints: tbs['basicConstraints'] = univ.Integer(basicConstraints).subtype(subtypeSpec=constraint.ValueRangeConstraint(0, 7))
        if certificatePolicy: tbs['certificatePolicy'] = univ.ObjectIdentifier(certificatePolicy)
        if subjectAltName: tbs['subjectAltName'] = subjectAltName
        if issuerAltName: tbs['issuerAltName'] = issuerAltName
        if extendedKeyUsage: tbs['extendedKeyUsage'] = univ.ObjectIdentifier(extendedKeyUsage)
        if authInfoAccessOCSP: tbs['authInfoAccessOCSP'] = char.IA5String(authInfoAccessOCSP)
        if cRLDistribPointURI: tbs['cRLDistribPointURI'] = char.IA5String(cRLDistribPointURI)
        if x509extensions: tbs['x509extensions'] = x509extensions
        return tbs


class Certificate(univ.Sequence, SequenceCouldmatchMixin):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 20))
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('tbsCertificate', TBSCertificate()),
        namedtype.NamedType('cACalcValue', univ.OctetString())
    )

    @staticmethod
    def new(tbsCertificate, cACalcValue):
        certificate = Certificate()
        certificate['tbsCertificate'] = tbsCertificate
        certificate['cACalcValue'] = cACalcValue

        return certificate


class ECDSA_Sig_Value_Y(univ.Choice, ChoiceCouldMatchMixin): # See [SEC1]
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('b', univ.Boolean()),
        namedtype.NamedType('f', univ.OctetString()), # FieldElement
    )

    @staticmethod
    def new(b=None, f=None):
        y = ECDSA_Sig_Value_Y()
        if b != None:
            y['b'] = univ.Boolean(value=b)
        if y:
            y['f'] = univ.OctetString(value=f)

        return y


class ECDSA_Sig_Value(univ.Sequence, SequenceCouldmatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('r', univ.Integer()),
        namedtype.NamedType('s', univ.Integer()),
        namedtype.NamedType('a', univ.Integer()),
        namedtype.NamedType('y', ECDSA_Sig_Value_Y()),
    )

    @staticmethod
    def new(r, s, a=None, y=None):
        sigval = ECDSA_Sig_Value()
        sigval['r'] = univ.Integer(r)
        sigval['s'] = univ.Integer(s)

        if a != None:
            sigval['a'] = univ.Integer(a)

        if y:
            sigval['y'] = y

        return sigval


class ECDSA_Full_R(univ.Sequence, SequenceCouldmatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('r', univ.OctetString()), #ECPoint as defined in section 2.3.3 of [SEC1]
        namedtype.NamedType('s', univ.Integer())
    )

    @staticmethod
    def new(r, s):
        full_r = ECDSA_Full_R()
        full_r['r'] = univ.OctetString(value=r)
        full_r['s'] = univ.Integer(value=s)

        return full_r


class ECDSA_Signature(univ.Choice, ChoiceCouldMatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('two-ints-plus', ECDSA_Sig_Value),
        namedtype.NamedType('point-int', ECDSA_Full_R),
    )

    @staticmethod
    def new(two_ints_plus=None, point_int=None):
        sig = ECDSA_Signature()
        if two_ints_plus:
            sig['two-ints-plus'] = two_ints_plus
        if point_int:
            sig['point-int'] = point_int

        return sig


class RSA_Signature(univ.OctetString): pass


class RSAPublicKey(univ.Sequence, SequenceCouldmatchMixin):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('n', univ.Integer()),
        namedtype.NamedType('e', univ.Integer())
    )

    @staticmethod
    def new(n, e):
        pubkey = RSAPublicKey()
        pubkey['n'] = univ.Integer(value=n)
        pubkey['e'] = univ.Integer(value=e)

        return pubkey


class AlgorithmObjectIdentifiers(enum.Enum):
    ecdsa_with_sha256_secp192r1     = univ.ObjectIdentifier("2.16.840.1.114513.1.0")
    ecdsa_with_sha256_secp224r1     = univ.ObjectIdentifier("2.16.840.1.114513.1.1")
    ecdsa_with_sha256_sect233k1     = univ.ObjectIdentifier("2.16.840.1.114513.1.2")
    ecdsa_with_sha256_sect233r1     = univ.ObjectIdentifier("2.16.840.1.114513.1.3")
    ecqv_with_sha256_secp192r1      = univ.ObjectIdentifier("2.16.840.1.114513.1.4")
    ecqv_with_sha256_secp224r1      = univ.ObjectIdentifier("2.16.840.1.114513.1.5")
    ecqv_with_sha256_sect233k1      = univ.ObjectIdentifier("2.16.840.1.114513.1.6")
    ecqv_with_sha256_sect233r1      = univ.ObjectIdentifier("2.16.840.1.114513.1.7")
    rsa_with_sha256                 = univ.ObjectIdentifier("2.16.840.1.114513.1.8")
    ecdsa_with_sha256_secp256r1     = univ.ObjectIdentifier("2.16.840.1.114513.1.9")
    ecqv_with_sha256_secp256r1      = univ.ObjectIdentifier("2.16.840.1.114513.1.10")

def generate_ec_private_key(curve='prime256v1', private_key_path='private.pem'):
    """openssl ecparam -genkey -name prime256v1 -out private.pem"""
    proc = subprocess.Popen(
        ['openssl', 'ecparam','-genkey', '-name', curve,'-out', private_key_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()

    if err:
        raise OSError(err)

def extract_ec_public_key(private_key_path='private.pem', public_key_path='public.pem'):
    """openssl ec -in private.pem -pubout -out public.pem"""
    proc = subprocess.Popen(
        ['openssl', 'ec', '-in', private_key_path, '-pubout', public_key_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()

    if not err:
        with open(public_key_path, 'rb') as signature_file:
            signature = signature_file.read()
            return signature
    else:
        raise OSError(err)

def generate_signature(to_be_signed_bytes, private_key_path='private.pem'):
    """openssl dgst -sha256 -sign private.pem -out signature.der message.txt"""
    byte_path = "/tmp/to_be_signed.tmp"
    with open(byte_path, 'wb') as byte_file:
        byte_file.write(to_be_signed_bytes)

    signature_path = "/tmp/signature.der"
    proc = subprocess.Popen(['openssl', 'dgst', '-sha256', '-sign', private_key_path, '-out', signature_path, byte_path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()

    if not err:
        with open(signature_path, 'rb') as signature_file:
            signature = signature_file.read()
            return signature
    else:
        raise OSError(err)

def verify_signature(signed_bytes, signature, public_key_path='public.pem'):
    """openssl dgst -sha256 -verify public.pem -signature signature.der message.txt"""
    byte_path = "/tmp/signed.tmp"
    with open(byte_path, 'wb') as byte_file:
        byte_file.write(signed_bytes)

    signature_path = "/tmp/signature.der"
    with open(signature_path, 'wb') as signature_file:
        signature_file.write(signature)

    proc = subprocess.Popen(['openssl', 'dgst', '-sha256', '-verify', public_key_path, '-signature', signature_path, byte_path],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()
    if not err:
        return out.strip() == b"Verified OK"
    else:
        raise OSError(err)

def certificate_to_m2m_der(certificate_path):
    pass

def m2m_certificate_to_file(certificate, certificate_path):
    with open(certificate_path, 'wb+') as cert_file:
        cert_file.write(b'------BEGIN CERTIFICATE------'+b'\n')
        cert_file.write(base64.encodebytes(der_encoder.encode(certificate)))
        cert_file.write(b'------END CERTIFICATE------')

def m2m_bytes_from_file(certificate_path):
    with open(certificate_path, 'rb') as cert_file:
        lines = cert_file.readlines()
        content_lines = lines[1:-1]
        content = b''.join(content_lines)
        return base64.decodebytes(content)

def sign_certificate(tbs_certificate, private_key_path='private.pem', as_bytes=False):
    tbs_cert_bytes = der_encoder.encode(tbs_certificate)
    signature_bytes = generate_signature(tbs_cert_bytes, private_key_path=private_key_path)

    cACalcValue = univ.OctetString(value=signature_bytes)
    certificate = Certificate.new(tbs_certificate, cACalcValue)

    if as_bytes:
        return der_encoder.encode(certificate)
    else:
        return certificate


DUMMY_SUBJECT = Name.new(AttributeValue(country='US'),
                         AttributeValue(organization='ACME corp.'),
                         #AttributeValue(stateOrProvince='New Jersey'),
                         AttributeValue(locality='Fairfield'))

DUMMY_TO_BE_SIGNED_CERTIFICATE = TBSCertificate.new(version=0,
                         serialNumber=int(123456789).to_bytes(20, byteorder='big'),
                         subject=DUMMY_SUBJECT,
                         cAAlgorithm="1.2.840.10045.4.3.2",
                         # ecdsaWithSha256: http://oid-info.com/get/1.2.840.10045.4.3.2
                         cAAlgParams=base64.decodebytes(b'BggqhkjOPQMBBw=='),  # EC PARAMETERS
                         # Parameters for the elliptic curve: http://oid-info.com/get/1.2.840.10045.3.1.7
                         issuer=DUMMY_SUBJECT,  # This is a self-signed certificate
                         pKAlgorithm="1.2.840.10045.4.3.2",  # Same as cAAlgorithm
                         pubKey=base64.decodebytes(
                             b'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEyCjVqzDqCn5KS2QYmD6bCajY1L8+\nla/50oJSDw5nKZm9zqeUIxwpl215Gz+aeBJOEHEC06fHjnb3TNdQcu1aKg=='),
                         subjKeyId=int(1).to_bytes(1, byteorder='big'),
                         # Key ID of the subject (which number do we give the private key?)
                         keyUsage=0b10100000.to_bytes(1, byteorder='big'),  # digitalSignature & keyEncipherment bit set
                         # See https://tools.ietf.org/html/rfc5280#section-4.2.1.3
                         certificatePolicy="2.5.29.32.0",  # Anypolicy: http://www.oid-info.com/get/2.5.29.32.0
                         )


if __name__ == '__main__':
    issuer = Name.new(AttributeValue(country='US'),
                      AttributeValue(organization='Big CAhuna burger'),
                      AttributeValue(locality='Los Angeles'),
                      AttributeValue(serialNumber='987654321'))
    der_encoder.encode(issuer)

    issuerAlternativeName = GeneralName.new(uniformResourceIdentifier="blabla.com")
    der_encoder.encode(issuerAlternativeName)

    subject = Name.new(AttributeValue(country='US'),
                       AttributeValue(organization='ACME corp.'),
                       # AttributeValue(stateOrProvince='New Jersey'),
                       AttributeValue(locality='Fairfield'))
    der_encoder.encode(subject)

    subjectAlternativeName = GeneralName.new(uniformResourceIdentifier="blabla.com")
    print(subjectAlternativeName.prettyPrint())
    der_encoder.encode(subjectAlternativeName)

    authkey = AuthKeyId.new(keyIdentifier=int(123456789).to_bytes(4, byteorder='big'),
                            authCertIssuer=subjectAlternativeName,
                            authCertSerialNum=int(123456789).to_bytes(4, byteorder='big'))
    print(authkey.prettyPrint())
    # import pudb; pudb.set_trace()
    # break /usr/local/lib/python3.5/dist-packages/pyasn1/type/univ.py:1124
    # break /usr/local/lib/python3.5/dist-packages/pyasn1/codec/ber/encoder.py:324
    der_encoder.encode(authkey)

    # How do signatures and the whole Public Key Infrastructure work? https://en.wikipedia.org/wiki/Public_key_certificate
    #
    # A Certificate Authority (the issuer) gives us (the subject) a certificate.
    # The CA signs the certificate with their private key. *Their* signature and *our* public key are included in *our* certificate.
    # Anyone can see the certificate with the signature and the public key and verify that those are valid.
    # In an NDEF Signature Record, the certificate is included within the Signature Record, or at least a reference to it.
    #
    # We take this certificate, have our own private key (paired with the public key in the certificate) and can make signatures using that private key.
    # To sign a message, we use a signing algorithm that uses the message and our private key. The signature will be sent along with the message.
    #
    # The public key (in the certificate) can be used to verify the signature:
    #   the combination of the message (signed data), the signature and the public key can only be valid if it was signed with our private key.
    #
    # For this test, we will simply use a public and private key, separate from a certificate.
    # The message we will be signing is "hello world".encode("ascii"), which is b'hello world' in Python
    #
    # For NDEF signatures, the only available hash type for signatures is SHA256.
    # We create a private key using
    # $ openssl ecparam -genkey -name prime256v1 -out private.pem
    # prime256v1 corresponds to AlgorithmObjectIdentifiers.ecdsa_with_sha256_secp256r1
    # and Signature Type / Hash Type ECDSA [DSS] P256 (I think)
    #
    # private.pem then contains:
    # -----BEGIN EC PARAMETERS-----
    # BggqhkjOPQMBBw==
    # -----END EC PARAMETERS-----
    # -----BEGIN EC PRIVATE KEY-----
    # MHcCAQEEIAMRJK6SAovUhcPFmmFxLLW4D1wTTXEqUFmMxYk5DfxdoAoGCCqGSM49
    # AwEHoUQDQgAEyCjVqzDqCn5KS2QYmD6bCajY1L8+la/50oJSDw5nKZm9zqeUIxwp
    # l215Gz+aeBJOEHEC06fHjnb3TNdQcu1aKg==
    # -----END EC PRIVATE KEY-----
    #
    # To get the public key matching the private key:
    # $ openssl ec -in private.pem -pubout -out public.pem
    # public.pem then contains:
    # -----BEGIN PUBLIC KEY-----
    # MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEyCjVqzDqCn5KS2QYmD6bCajY1L8+
    # la/50oJSDw5nKZm9zqeUIxwpl215Gz+aeBJOEHEC06fHjnb3TNdQcu1aKg==
    # -----END PUBLIC KEY-----
    #
    #
    # Signing a message:
    # To then sign the message, we take the sha256 hash of it and then calculate the signature over the hash:
    # Write the message to a file message.txt, then
    # $ openssl dgst -sha256 -sign private.pem -out signature.der message.txt
    #
    # To verify, we take the sha256 of the message and that the signature matches with that hash & the public key
    # $ openssl dgst -sha256 -verify public.pem -signature signature.der message.txt
    # The content of signature.bin then is already DER encoded and contains 2 integers
    #   (http://davidederosa.com/basic-blockchain-programming/elliptic-curve-digital-signatures/ and
    #   verified with https://lapo.it/asn1js/#30450220362442B5E0293651BCD53E1F0E68145B17E323BD5BF09ECF49F307C82E44A0EF02210083DB95FE17C5C58B7DCD377972508645B3C49ECB9A42808573761982E76FAAFA)
    # This matches the specification of ECDSA-Signature with the ECDSA-Sig-Value option.

    # cACalcValue must contain the CA's (but for now our own) signature over the certificate.
    # To do this:
    # Generate a certificate and sign that with the private key (which happens to be of that same certificate)
    # $ openssl req -new -key private.pem -out to_be_signed_certificate.csr -subj '/C=US/ST=New Jersey/L=Fairfield/CN=www.acme.com/'
    # $ openssl dgst -sha256 -sign private.pem -out certificate_signature.der to_be_signed_certificate.csr
    # *That* signature should go below!
    # The signature is calculated over the TBSCertificate, DER encoded.

    # The certificate, manually parsed into this form:
    tbs = TBSCertificate.new(version=0,
                             serialNumber=int(123456789).to_bytes(20, byteorder='big'),
                             subject=subject,
                             cAAlgorithm="1.2.840.10045.4.3.2",
                             # ecdsaWithSha256: http://oid-info.com/get/1.2.840.10045.4.3.2
                             cAAlgParams=base64.decodebytes(b'BggqhkjOPQMBBw=='), # EC PARAMETERS
                             # Parameters for the elliptic curve: http://oid-info.com/get/1.2.840.10045.3.1.7
                             issuer=subject,  # This is a self-signed certificate
                             # validFrom=int(123456789).to_bytes(4, byteorder='big'), # seconds since epoch, optional
                             # validDuration=int(123456789).to_bytes(4, byteorder='big'),  # seconds since validFrom, optional
                             pKAlgorithm="1.2.840.10045.4.3.2",  # Same as cAAlgorithm
                             # pKAlgParams="1.2.3.4", #Optional
                             pubKey=base64.decodebytes(b'MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEyCjVqzDqCn5KS2QYmD6bCajY1L8+\nla/50oJSDw5nKZm9zqeUIxwpl215Gz+aeBJOEHEC06fHjnb3TNdQcu1aKg=='),
                             # authKeyId=authkey, optional, See https://tools.ietf.org/html/rfc5280#section-4.2.1.1 for explanation
                             subjKeyId=int(1).to_bytes(1, byteorder='big'),  # Key ID of the subject (which number do we give the private key?)
                             keyUsage=0b10100000.to_bytes(1, byteorder='big'), # digitalSignature & keyEncipherment bit set
                             # See https://tools.ietf.org/html/rfc5280#section-4.2.1.3
                             certificatePolicy="2.5.29.32.0",  # Anypolicy: http://www.oid-info.com/get/2.5.29.32.0
                             # subjectAltName=subjectAlternativeName, #optional
                             # issuerAltName=issuerAlternativeName, #Optional
                             extendedKeyUsage="2.16.840.1.114513.29.37", # Optional in ASN1 but explanation in spec says it MUST be present. Variant of X509 http://www.oid-info.com/get/2.5.29.37.0
                             # cRLDistribPointURI=u'www.certificatebegone.com/' # Optional
                             )
    import hashlib

    print(hashlib.sha224(der_encoder.encode(tbs)).hexdigest())

    certificate = sign_certificate(tbs, private_key_path='private.pem')

    print(certificate.prettyPrint())
    print(binascii.hexlify(der_encoder.encode(certificate)))
    print(len(der_encoder.encode(certificate)))

    m2m_certificate_to_file(certificate, 'm2m_certificate.pem')


