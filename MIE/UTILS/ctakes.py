import os

from lxml import etree, html
import subprocess
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class cTakes():
    def _write_to_engine(self, text):
        """Write medical text into ctakes-path/note_input/note.txt
        - Args:
            text: medical text to be process
        """
        input_path = os.environ.get("CTAKES_PATH") + "/note_input/note.txt"
        with open(input_path, 'w') as f:
            f.write(text)
    
    def _run_sh(self):
        """Run sh to process input
        """
        shell_path = os.environ.get("CTAKES_PATH") + "/bin/runctakesCPE_CLI.sh"
        subprocess.call([shell_path])

    def _etree_to_dict(self, t):
        """
        """
        d = {t.tag : map(self._etree_to_dict, t.iterchildren())}
        d.update(('@' + k, v) for k, v in t.attrib.iteritems())
        d['text'] = t.text
        return d

    def _parse_output(self, text):
        """Parse output of annotation result
        """
        output_path = os.environ.get("CTAKES_PATH") + "/result_output/note.txt.xml"
        doc = etree.parse(output_path)
        matched_elem = []
        for elem in doc.iter():
            if "Mention" in elem.tag:
                matched_elem.append(self._etree_to_dict(elem))
        for d in matched_elem:
            d['text'] = text[int(d['@begin']):int(d['@end']) + 1].strip()
        return matched_elem

    def pipeline(self, text):
        """cTakes pipline, write, run and parse
        - Args:
            text: medical text input, string
        - Returns:
            result: extracted output
        """
        text = text.encode('utf-8').strip()
        self._write_to_engine(text)
        self._run_sh()
        result = self._parse_output(text)
        return result
